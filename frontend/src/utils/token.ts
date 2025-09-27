const ACCESS_TOKEN_COOKIE = "access_token";

const getCookie = (name: string): string | null => {
	if (typeof document === "undefined") return null;

	const cookies = document.cookie.split("; ");
	for (const cookie of cookies) {
		const [cookieName, ...valueParts] = cookie.split("=");
		if (cookieName === name) {
			const value = valueParts.join("="); // Handle JWT tokens with = signs
			return value || "";
		}
	}
	return null;
};

const setCookie = (name: string, value: string): void => {
	if (typeof document === "undefined") return;

	const isProduction = process.env.NODE_ENV === "production";
	const secureFlag = isProduction ? "; Secure" : "";
	const sameSite = isProduction ? "; SameSite=Strict" : "; SameSite=Lax";

	// Try setting without URL encoding first for JWTs
	const cookieString = `${name}=${value}; path=/${sameSite}${secureFlag}`;
	document.cookie = cookieString;
};

const clearCookie = (name: string): void => {
	if (typeof document === "undefined") return;

	document.cookie = `${name}=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT`;
};

export const getAccessToken = (): string | null => {
	const token = getCookie(ACCESS_TOKEN_COOKIE);
	return token;
};

export const setAccessToken = (token: string): void => {
	setCookie(ACCESS_TOKEN_COOKIE, token);
};

export const clearAccessToken = (): void => {
	clearCookie(ACCESS_TOKEN_COOKIE);
};

export const isLoggedIn = (): boolean => {
	return getAccessToken() !== null;
};
