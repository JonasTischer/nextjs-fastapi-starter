import {
	authJwtLoginMutation,
	authJwtLogoutMutation,
	registerRegisterMutation,
} from "@/generated/backend-client/@tanstack/react-query.gen";
import { handleApiError } from "@/utils/error-handler";
import { clearAccessToken, setAccessToken } from "@/utils/token";
import { useMutation } from "@tanstack/react-query";
import { useRouter } from "next/navigation";
import { toast } from "sonner";

export function useLogin() {
	const router = useRouter();
	return useMutation({
		...authJwtLoginMutation(),
		onSuccess: (data) => {
			setAccessToken(data.access_token);
			router.push("/dashboard");
			toast.success("Logged in successfully!");
		},
		onError: (error) => {
			handleApiError(error, "Login failed");
		},
	});
}

export function useLogout() {
	const router = useRouter();

	return useMutation({
		...authJwtLogoutMutation(),
		onSuccess: () => {
			clearAccessToken();
			router.push("/");
		},
	});
}

export function useSignUp() {
	const login = useLogin();
	const router = useRouter();
	return useMutation({
		...registerRegisterMutation(),
		onSuccess: (
			data,
			variables: { body: { email: string; password: string } },
		) => {
			toast.success("Account created successfully!");
			if (variables?.body?.email && variables?.body?.password) {
				// Auto-login after successful registration
				login.mutate({
					body: {
						username: variables.body.email,
						password: variables.body.password,
					},
				});
			} else {
				toast.error(
					"Account created, but auto-login failed. Please log in manually.",
				);
				router.push("/login");
			}
		},
		onError: (error) => {
			handleApiError(error, "Sign up failed");
		},
	});
}
