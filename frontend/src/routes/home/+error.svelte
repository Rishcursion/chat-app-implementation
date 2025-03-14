<script lang="ts">
	import { fly } from 'svelte/transition';
</script>

<div
	class="bg-background flex min-h-screen items-center justify-center p-4"
	in:fly={{ y: 20, duration: 500 }}
>
	<div class="w-full max-w-md">
		<div
			class="rounded-2xl border border-white/10 bg-white/5 p-8 text-center backdrop-blur-lg"
			in:fly={{ y: 20, duration: 500, delay: 200 }}
		>
			<!-- Error Icon -->

			<!-- Error Message -->
			<h1
				class="text-headline mb-4 text-2xl font-bold"
				in:fly={{ y: 20, duration: 500, delay: 400 }}
			>
				Session Expired
			</h1>

			<p class="text-paragraph mb-8" in:fly={{ y: 20, duration: 500, delay: 600 }}>
				Uh Oh! Your session has expired. Please log in again to continue using the application.
			</p>

			<!-- Action Button -->
			<form action="?/dispose_stale_cookies" method="POST">
				<button
					type="submit"
					class="bg-button text-button-text shadow-button/20 w-1/3 transform rounded-lg p-2 font-semibold shadow-lg
               transition-all duration-300 hover:scale-105
               hover:opacity-90 active:scale-95"
					in:fly={{ y: 20, duration: 500, delay: 800 }}
				>
					Log In Again
				</button>
			</form>

			<!-- Additional Info -->
			<p class="text-paragraph pt-6 text-sm" in:fly={{ y: 20, duration: 500, delay: 1000 }}>
				If this keeps happening, try clearing your browser cache or contact support.
			</p>
		</div>
	</div>
</div>
