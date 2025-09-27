"use client";

import {
	BadgeCheck,
	Bell,
	ChevronsUpDown,
	CreditCard,
	LogOut,
	Sparkles,
} from "lucide-react";

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuGroup,
	DropdownMenuItem,
	DropdownMenuLabel,
	DropdownMenuSeparator,
	DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
	SidebarMenu,
	SidebarMenuButton,
	SidebarMenuItem,
	useSidebar,
} from "@/components/ui/sidebar";
import { useLogout } from "@/tanstack/features/auth/mutations";
import type { UserRead } from "@/generated/backend-client/types.gen";

export function NavUser({
	user,
}: {
	user: UserRead;
}) {
	const avatar_url = "https://github.com/shadcn.png";
	const account_type = "Premium Account";
	const { isMobile } = useSidebar();
	const userInitials =
		`${user?.email?.[0] ?? ""}${user?.email?.[0] ?? ""}`.toUpperCase();

	const logout = useLogout();

	return (
		<SidebarMenu>
			<SidebarMenuItem>
				<DropdownMenu>
					<DropdownMenuTrigger asChild>
						<SidebarMenuButton className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground">
							<div className="rounded-lg bg-accent/50 flex items-center gap-3">
								<Avatar className="h-10 w-10 border">
									{/* Add actual image source if available */}
									<AvatarImage src={avatar_url} alt={user?.email ?? "User"} />
									<AvatarFallback className="bg-gradient-to-br from-medical-teal to-medical-blue text-white font-medium">
										{userInitials || "???"} {/* Fallback initials */}
									</AvatarFallback>
								</Avatar>
								<div>
									<p className="text-sm font-semibold text-foreground">
										{user?.email ? `${user.email}` : "Loading..."}
									</p>
									<p className="text-xs text-muted-foreground">
										{account_type || "Premium Account"}{" "}
										{/* Example dynamic field */}
									</p>
								</div>
							</div>
							<ChevronsUpDown className="ml-auto size-4" />
						</SidebarMenuButton>
					</DropdownMenuTrigger>
					<DropdownMenuContent
						className="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg"
						side={isMobile ? "bottom" : "right"}
						align="end"
						sideOffset={4}
					>
						<DropdownMenuLabel className="p-0 font-normal">
							<div className="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
								<Avatar className="h-10 w-10 border">
									{/* Add actual image source if available */}
									<AvatarImage src={avatar_url} alt={user?.email ?? "User"} />
									<AvatarFallback className="bg-gradient-to-br from-medical-teal to-medical-blue text-white font-medium">
										{userInitials || "???"} {/* Fallback initials */}
									</AvatarFallback>
								</Avatar>
								<div className="grid flex-1 text-left text-sm leading-tight">
									<span className="truncate font-semibold">{user.email}</span>
									<span className="truncate text-xs">{user.email}</span>
								</div>
							</div>
						</DropdownMenuLabel>
						<DropdownMenuSeparator />
						<DropdownMenuGroup>
							<DropdownMenuItem>
								<Sparkles />
								Upgrade to Pro
							</DropdownMenuItem>
						</DropdownMenuGroup>
						<DropdownMenuSeparator />
						<DropdownMenuGroup>
							<DropdownMenuItem>
								<BadgeCheck />
								Account
							</DropdownMenuItem>
							<DropdownMenuItem>
								<CreditCard />
								Billing
							</DropdownMenuItem>
							<DropdownMenuItem>
								<Bell />
								Notifications
							</DropdownMenuItem>
						</DropdownMenuGroup>
						<DropdownMenuSeparator />

						<DropdownMenuItem onClick={() => logout.mutate({})}>
							<LogOut />
							Logout
						</DropdownMenuItem>
					</DropdownMenuContent>
				</DropdownMenu>
			</SidebarMenuItem>
		</SidebarMenu>
	);
}
