<script lang="ts">
	import { fade, fly } from 'svelte/transition';
	import { quartIn, quartOut } from 'svelte/easing';
	import { enhance } from '$app/forms';
	import { onMount } from 'svelte';
	let isLogin = $state(false);
	let { data, form } = $props();
	let formAction: string = '?/register';
	function handle_switch() {
		// Decides whether the login or register page should be shown,
		window.location.href = '/auth/login';
	}
	onMount(() => (isLogin = true));
</script>

<main class="bg-background flex min-h-screen items-center justify-center">
	{#if isLogin}
		<!-- main container -->
		<div
			in:fly={{ easing: quartIn, duration: 1000, y: 100 }}
			class="flex max-w-md flex-col items-center justify-start rounded-xl bg-white/10 p-6 text-center backdrop-blur-lg md:w-3/4"
		>
			<h1 class="text-headline text-4xl font-bold">Welcome!</h1>
			<p class="text-paragraph w-3/4 pt-2 text-lg">
				Before you can start texting, we need to setup your account!
			</p>
			{#if form?.error}
				<p class="text-red-500">{form.error}</p>
			{/if}
			<!-- login form -->
			<form class="mt-10 flex flex-col" method="POST" action={formAction} use:enhance>
				<!-- login button -->
				<div class="flex flex-col items-start">
					<label for="username" class="text-headline text-lg font-semibold">Username</label>
					<input
						name="username"
						type="text"
						required
						maxlength="64"
						class="text-paragraph focus:border-button text-md my-2 transform rounded-lg border-2 bg-white/5 p-2 transition-colors ease-in"
						placeholder="Enter Username (max 64 chars)"
					/>
				</div>
				<div class="flex flex-col items-start">
					<label for="password" class="text-headline text-lg font-semibold">Password</label>
					<input
						name="password"
						type="password"
						required
						class="text-paragraph focus:border-button text-md my-2 transform rounded-lg border-2 bg-white/5 p-2 transition-colors ease-in"
						placeholder="Enter Password"
					/>
				</div>
				<div class="flex flex-col items-start">
					<label for="re_password" class="text-headline text-lg font-semibold"
						>Re-Enter Password</label
					>
					<input
						name="re_password"
						type="password"
						required
						class="text-paragraph focus:border-button text-md my-2 transform rounded-lg border-2 bg-white/5 p-2 transition-colors ease-in"
						placeholder="Enter Your Password Again"
					/>
				</div>
				<button
					type="submit"
					class="bg-button text-button-text mt-4 transform items-center rounded-lg p-2 text-xl font-semibold transition-all delay-100 ease-in hover:scale-105 hover:text-white active:scale-95"
					>Register!</button
				>
				<button
					onclick={handle_switch}
					type="button"
					class="hover:text-button text-paragraph mt-4 delay-100 ease-in">Returning User?</button
				>
			</form>
		</div>
	{/if}
</main>
