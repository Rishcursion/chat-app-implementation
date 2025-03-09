<script lang="ts">
	import { onMount } from 'svelte';
	import { quintOut } from 'svelte/easing';
	import { fly } from 'svelte/transition';
	let isMenuOpen = true;
	// your script goes here
	let isMounted = false;
	onMount(() => {
		isMounted = true;
	});
</script>

<main class="min-h-full">
	<!-- main sidebar -->
	<aside class="fixed top-0 left-0 h-full w-1/4 bg-white/10 backdrop-blur-md">
		<!-- user profile -->
	</aside>
</main>
