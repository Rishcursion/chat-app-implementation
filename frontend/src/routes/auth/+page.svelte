<script lang="ts">
	import { fade } from 'svelte/transition';
	import { quartIn } from 'svelte/easing';
	let isLogin = true;
	function handle_switch() {
		isLogin = !isLogin;
	}
</script>

{#if isLogin}
	<!-- main container -->
	<div
		class=" flex max-w-md flex-col items-center justify-start rounded-xl bg-white/10 p-6 text-center backdrop-blur-lg md:w-3/4"
		in:fade={{ easing: quartIn, duration: 1000 }}
	>
		<h1 class="text-headline text-4xl font-bold">Welcome Back</h1>
		<p class="text-paragraph w-1/2 pt-2 text-lg">We missed you, so did your friends!</p>
		<!-- login form -->
		<form action="post" class="mt-10 flex flex-col">
			<!-- login button -->
			<div class="flex flex-col items-start">
				<label for="username" class="text-headline text-lg font-semibold">Username</label>
				<input
					id="username"
					type="text"
					class="text-paragraph focus:border-button text-md my-2 transform rounded-lg border-2 bg-white/5 p-2 transition-colors ease-in"
					placeholder="Enter Username (max 64 chars)"
				/>
			</div>
			<div class="flex flex-col items-start">
				<label for="password" class="text-headline text-lg font-semibold">Password</label>
				<input
					id="password"
					type="password"
					class="text-paragraph focus:border-button text-md my-2 transform rounded-lg border-2 bg-white/5 p-2 transition-colors ease-in"
					placeholder="Enter Password"
				/>
			</div>
			<button class="hover:text-button text-paragraph mt-4 delay-100 ease-in"
				>Forgot Password?</button
			>
			<button
				class="bg-button text-button-text mt-4 transform items-center rounded-lg p-2 text-xl font-semibold transition-all delay-100 ease-in hover:scale-105 hover:text-white active:scale-95"
				>Log In!</button
			>
			<button
				on:click={handle_switch}
				type="button"
				class="hover:text-button text-paragraph mt-4 delay-100 ease-in">New User?</button
			>
		</form>
	</div>
{:else}
	<!-- main container -->
	<div
		in:fade={{ easing: quartIn, duration: 1000 }}
		class="flex max-w-md flex-col items-center justify-start rounded-xl bg-white/10 p-6 text-center backdrop-blur-lg md:w-3/4"
	>
		<h1 class="text-headline text-4xl font-bold">Welcome!</h1>
		<p class="text-paragraph w-1/2 pt-2 text-lg">
			Before you can start texting, we need to setup your account!
		</p>
		<!-- login form -->
		<form action="post" class="mt-10 flex flex-col">
			<!-- login button -->
			<div class="flex flex-col items-start">
				<label for="username" class="text-headline text-lg font-semibold">Username</label>
				<input
					id="username"
					type="text"
					class="text-paragraph focus:border-button text-md my-2 transform rounded-lg border-2 bg-white/5 p-2 transition-colors ease-in"
					placeholder="Enter Username (max 64 chars)"
				/>
			</div>
			<div class="flex flex-col items-start">
				<label for="password" class="text-headline text-lg font-semibold">Password</label>
				<input
					id="password"
					type="password"
					class="text-paragraph focus:border-button text-md my-2 transform rounded-lg border-2 bg-white/5 p-2 transition-colors ease-in"
					placeholder="Enter Password"
				/>
			</div>
			<div class="flex flex-col items-start">
				<label for="password" class="text-headline text-lg font-semibold">Re-Enter Password</label>
				<input
					id="password"
					type="password"
					class="text-paragraph focus:border-button text-md my-2 transform rounded-lg border-2 bg-white/5 p-2 transition-colors ease-in"
					placeholder="Enter Password"
				/>
			</div>
			<button
				class="bg-button text-button-text mt-4 transform items-center rounded-lg p-2 text-xl font-semibold transition-all delay-100 ease-in hover:scale-105 hover:text-white active:scale-95"
				>Register!</button
			>
			<button
				on:click={handle_switch}
				type="button"
				class="hover:text-button text-paragraph mt-4 delay-100 ease-in">Returning User?</button
			>
		</form>
	</div>
{/if}
