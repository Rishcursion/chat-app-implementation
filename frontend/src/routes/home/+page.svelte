<script lang="ts">
	import { onMount } from 'svelte';
	import { quintOut } from 'svelte/easing';
	import { fly } from 'svelte/transition';
	let isMenuOpen = $state(true);
	let isGroup = $state(false);
	let isDM = $state(true);
	// your script goes here
	let isMounted = false;
	onMount(() => {
		isMounted = true;
	});
</script>

<main class="bg-background min-h-screen min-w-screen">
	<!-- sidebar -->
	<aside
		class="fixed inset-0 z-50 flex h-screen w-1/5 shrink-0 flex-col bg-white/10 backdrop-blur-lg lg:relative"
	>
		<div class="space-y-4 p-4">
			<!-- User Profile -->
			<div
				class="flex flex-col items-center justify-center rounded-lg bg-white/5 p-4 backdrop-blur-lg"
			>
				<div
					class="bg-illustration-highlight flex h-16 w-16 items-center justify-center rounded-full text-xl"
				>
					JD
				</div>
			</div>
		</div>
	</aside>
</main>
