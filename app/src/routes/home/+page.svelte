<script lang="ts">
	import ChatWindow from '$lib/components/chat_window.svelte';
	import Sidebar from '$lib/components/sidebar.svelte';
	import { chatting_with, current_user } from '$lib/store/globalState';
	type UserData = {
		username: string;
		invite_code: string;
	};
	type test = {
		chat_id: number;
		username: string;
		timestamp: string;
		message_head: string;
		messages: {
			content: string;
			sender: string;
			time: string;
		}[];
	};
	let { data }: { data: any; user?: UserData } = $props();
	// User Details
	let username: string = data.user.username;
	let invite_code: string = data.user.invite_code;
	current_user.set(data.user.user_id);
	//Test data
	const user_data: test[] = [
		{
			chat_id: 1,
			username: 'test1',
			timestamp: '2025-03-14 15:13',
			message_head: 'Hey, how are you?',
			messages: [
				{ content: 'Hey, how are you?', sender: 'test1', time: '15:13' },
				{ content: 'I was thinking about our last trip.', sender: 'test1', time: '15:14' },
				{ content: 'Do you remember the beach sunset?', sender: 'test1', time: '15:15' },
				{ content: 'It was such a great moment!', sender: 'test1', time: '15:16' },
				{ content: 'We should plan something similar again.', sender: 'test1', time: '15:17' },
				{ content: 'Maybe a camping trip this time?', sender: 'test1', time: '15:18' },
				{ content: 'Let me know what you think.', sender: 'test1', time: '15:19' },
				{ content: 'By the way, did you watch the new movie?', sender: 'test1', time: '15:20' },
				{ content: 'I heard it got great reviews.', sender: 'test1', time: '15:21' },
				{ content: 'I’m planning to watch it this weekend.', sender: 'test1', time: '15:22' },
				{ content: 'Let’s catch up soon.', sender: 'test1', time: '15:23' },
				{ content: 'Also, I need your help with something.', sender: 'test1', time: '15:24' },
				{ content: 'I’m working on a new project.', sender: 'test1', time: '15:25' },
				{ content: 'It’s a mobile app idea.', sender: 'test1', time: '15:26' },
				{ content: 'Would love to get your feedback.', sender: 'test1', time: '15:27' },
				{ content: 'We could meet for coffee and discuss.', sender: 'test1', time: '15:28' },
				{ content: 'I’ll send you the details soon.', sender: 'test1', time: '15:29' },
				{
					content: 'Have you been reading any good books lately?',
					sender: 'test1',
					time: '15:30'
				},
				{ content: 'I just finished an amazing one.', sender: 'test1', time: '15:31' },
				{ content: 'I think you’d really enjoy it.', sender: 'test1', time: '15:32' },
				{ content: 'Alright, talk to you later!', sender: 'test1', time: '15:33' }
			]
		},
		{
			chat_id: 2,
			username: 'test2',
			timestamp: '2025-03-14 15:13',
			message_head: 'Hey, how are you?',
			messages: [
				{ content: 'Hey, how are you?', sender: 'test1', time: '15:13' },
				{ content: 'I was thinking about our last trip.', sender: 'test1', time: '15:14' },
				{ content: 'Do you remember the beach sunset?', sender: 'test1', time: '15:15' }
			]
		}
	];
</script>

<main class="bg-background flex min-h-screen min-w-screen flex-row">
	<!-- sidebar -->
	<Sidebar {username} {invite_code} {user_data} />
	<!-- chat section -->
	{#if $chatting_with != -1}
		<ChatWindow {user_data} active_chat={$chatting_with} />
	{:else}
		<div class="flex h-screen w-4/5 items-center justify-center">
			<div class="w-max">
				<p
					class="text-headline border-r-headline animate-typing overflow-hidden border-r-2 text-3xl whitespace-nowrap"
				>
					Select A Chat To Start Texting
				</p>
			</div>
		</div>
	{/if}
</main>
