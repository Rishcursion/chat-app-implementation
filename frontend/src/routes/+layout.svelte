<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<main class="bg-background flex min-h-screen items-center justify-center">
	{@render children()}
</main>
