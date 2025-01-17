import moment from "moment";
import momentJa from "moment-jalaali";
import momentTz from "moment-timezone";

export function addCommaToNumber(value) {
  return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

export function capitalizeWord(value) {
  return value.charAt(0).toUpperCase() + value.slice(1);
}

export const convertPersianToEnglish = (persianDate) => {
  const persianDigits = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];
  const englishDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

  return persianDate.replace(/[۰-۹]/g, (char) => {
    const index = persianDigits.indexOf(char);
    return englishDigits[index];
  });
};

export const convertJalaliToGregorian = (jalaliDate) => {
  // Parse the Jalali date and format it as Gregorian
  return moment(jalaliDate, "jYYYY/jMM/jDD").toLocaleString("en", {
    timeZone: "Asia/Tehran",
  });
};

export const convertJalaliToGregorianISO = (jalaliDate) => {
  // Parse the Jalali date
  const gregorianDate = momentJa(jalaliDate, "jYYYY/jMM/jDD"); // Convert to Gregorian internally

  // Apply the timezone
  // const dateInTimezone = momentTz.tz(gregorianDate, "America/New_York");

  // Convert to ISO string
  return gregorianDate.toISOString();
};
