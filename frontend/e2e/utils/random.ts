export function randomEmail() {
  return `playwright-${Math.random().toString(36).slice(2, 10)}@example.com`;
}

export function randomPassword() {
  const suffix = Math.random().toString(36).slice(2, 8);
  return `P@ss${suffix}A!`;
}
