<script lang="ts">
	import { onMount } from 'svelte';
	import { quintIn } from 'svelte/easing';
	import { fly } from 'svelte/transition';
	type component_props = {
		username: string;
		timestamp: string;
		message_head: string;
		idx: number;
	};
	let { username, timestamp, message_head, idx }: component_props = $props();
	let isMount = false;
	onMount(() => {
		isMount = true;
	});
</script>

<div
	class=" bg-illustration-main/10 border-illustration-main my-2 ml-4 flex w-9/10 flex-row items-center justify-start rounded-lg border-2 p-2 backdrop-blur-3xl"
>
	<div
		class="bg-illustration-highlight flex h-8 w-8 shrink grow-0 items-center justify-center rounded-full text-xl"
	>
		{username.charAt(0).toUpperCase()}
	</div>
	<div class=" flex flex-col">
		<h3 class="text-paragraph mx-2 text-lg font-semibold">{username}</h3>
		<p class="text-paragraph mx-2 text-sm text-wrap opacity-80">{message_head}</p>
	</div>
	<p class="text-paragraph fixed right-2 bottom-2 text-sm">{timestamp}</p>
</div>
