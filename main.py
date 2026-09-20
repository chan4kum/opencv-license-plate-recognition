import argparse
import cv2
import pytesseract

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--image", required=True)
    args = p.parse_args()

    img = cv2.imread(args.image)
    if img is None:
        raise SystemExit(f"Could not read {args.image}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = cascade.detectMultiScale(gray, 1.1, 4, minSize=(60, 20))
    for x, y, w, h in plates:
        roi = gray[y:y + h, x:x + w]
        roi = cv2.resize(roi, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
        roi = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        text = pytesseract.image_to_string(roi, config="--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789").strip()
        print("Plate:", text or "(unreadable)")
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, text, (x, max(20, y - 8)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    if len(plates) == 0:
        print("No plates found.")
    cv2.imshow("License Plate Recognition", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
