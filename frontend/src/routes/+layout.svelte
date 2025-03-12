<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<main class="bg-background min-h-screen min-w-screen">
	{@render children()}
</main>
