export function addCommaToNumber(value) {
  return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

export function capitalizeWord(value) {
  return value.charAt(0).toUpperCase() + value.slice(1);
}
