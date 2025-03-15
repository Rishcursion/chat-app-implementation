<script lang="ts">
	import { onMount } from 'svelte';
	import { quintIn } from 'svelte/easing';
	import { fly } from 'svelte/transition';
	type component_props = {
		username: string;
		timestamp: string;
		message_head: string;
		is_active: boolean;
	};
	let { username, timestamp, message_head, is_active }: component_props = $props();
	let isMount = false;
	onMount(() => {
		isMount = true;
	});
</script>

<div
	class="{is_active
		? 'border-button bg-illustration-main/20 '
		: 'bg-illustration-main/10 border-illustration-main'} my-2 ml-4 flex w-9/10 flex-row items-center justify-start rounded-lg border-2 p-2 backdrop-blur-3xl transition-colors delay-100 ease-in"
>
	<div
		class="bg-illustration-highlight flex h-8 w-8 shrink grow-0 items-center justify-center rounded-full text-xl"
	>
		{username.charAt(0).toUpperCase()}
	</div>
	<div class=" ml-2 flex flex-col">
		<h3 class="text-paragraph w-max text-lg font-semibold">{username}</h3>
		<p class="text-paragraph text-sm">
			{message_head.length > 30 ? message_head.slice(0, 30) + '...' : message_head}
		</p>
	</div>
	<p class="text-paragraph fixed top-2 right-2 text-sm">{timestamp}</p>
</div>
