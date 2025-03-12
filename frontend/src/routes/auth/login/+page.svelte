<script lang="ts">
	import { fade, fly } from 'svelte/transition';
	import { quartIn, quartOut } from 'svelte/easing';
	import { enhance } from '$app/forms';
	import { onMount } from 'svelte';
	let { data, form } = $props();
	let isLogin = $state(false);
	function handle_switch() {
		window.location.href = '/auth/register';
	}
	onMount(() => (isLogin = true));
</script>

<main class="flex min-h-screen min-w-screen items-center justify-center">
	{#if isLogin}
		<!-- main container -->
		<div
			class=" flex flex-col items-center justify-start rounded-xl bg-white/10 p-6 text-center backdrop-blur-lg md:w-3/4 lg:w-1/4"
			in:fly={{ easing: quartIn, duration: 1000, y: 100 }}
		>
			<h1 class="text-headline text-4xl font-bold">Welcome Back</h1>
			<p class="text-paragraph w-1/2 pt-2 text-lg">We missed you, so did your friends!</p>
			<!-- login form -->
			<form class="mt-10 flex flex-col" use:enhance method="POST" action="?/login">
				{#if form?.error}
					<p class="text-red-500">{form.error}</p>
				{/if}
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
				<button class="hover:text-button text-paragraph mt-4 delay-100 ease-in"
					>Forgot Password?</button
				>
				<button
					type="submit"
					class="bg-button text-button-text mt-4 transform items-center rounded-lg p-2 text-xl font-semibold transition-all delay-100 ease-in hover:scale-105 hover:text-white active:scale-95"
					>Log In!</button
				>
				<button
					onclick={handle_switch}
					type="button"
					class="hover:text-button text-paragraph mt-4 delay-100 ease-in">New User?</button
				>
			</form>
		</div>
	{/if}
</main>
