<script lang="ts">
	import ChatWindow from '$lib/components/chat_window.svelte';
	import Sidebar from '$lib/components/sidebar.svelte';
	import { activeChat } from '$lib/store/globalState';
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
	//Test data
	const user_data: test[] = [
		{
			chat_id: 20301991,
			username: 'John Doe',
			timestamp: '2025-03-14 15:13',
			message_head: 'Hey, how are you?',
			messages: [
				{ content: 'Hey, how are you?', sender: 'John Doe', time: '15:13' },
				{ content: 'I was thinking about our last trip.', sender: 'John Doe', time: '15:14' },
				{ content: 'Do you remember the beach sunset?', sender: 'John Doe', time: '15:15' },
				{ content: 'It was such a great moment!', sender: 'John Doe', time: '15:16' },
				{ content: 'We should plan something similar again.', sender: 'John Doe', time: '15:17' },
				{ content: 'Maybe a camping trip this time?', sender: 'John Doe', time: '15:18' },
				{ content: 'Let me know what you think.', sender: 'John Doe', time: '15:19' },
				{ content: 'By the way, did you watch the new movie?', sender: 'John Doe', time: '15:20' },
				{ content: 'I heard it got great reviews.', sender: 'John Doe', time: '15:21' },
				{ content: 'I’m planning to watch it this weekend.', sender: 'John Doe', time: '15:22' },
				{ content: 'Let’s catch up soon.', sender: 'John Doe', time: '15:23' },
				{ content: 'Also, I need your help with something.', sender: 'John Doe', time: '15:24' },
				{ content: 'I’m working on a new project.', sender: 'John Doe', time: '15:25' },
				{ content: 'It’s a mobile app idea.', sender: 'John Doe', time: '15:26' },
				{ content: 'Would love to get your feedback.', sender: 'John Doe', time: '15:27' },
				{ content: 'We could meet for coffee and discuss.', sender: 'John Doe', time: '15:28' },
				{ content: 'I’ll send you the details soon.', sender: 'John Doe', time: '15:29' },
				{
					content: 'Have you been reading any good books lately?',
					sender: 'John Doe',
					time: '15:30'
				},
				{ content: 'I just finished an amazing one.', sender: 'John Doe', time: '15:31' },
				{ content: 'I think you’d really enjoy it.', sender: 'John Doe', time: '15:32' },
				{ content: 'Alright, talk to you later!', sender: 'John Doe', time: '15:33' }
			]
		},
		{
			chat_id: 20301981,
			username: 'John',
			timestamp: '2025-03-14 15:13',
			message_head:
				'i want to meet you then eat fries while watching movies and chilling with ice cream.',
			messages: [
				{ content: 'Hey, are you free today?', sender: 'John', time: '15:00' },
				{
					content: 'I want to meet you then eat fries while watching movies.',
					sender: 'John',
					time: '15:13'
				},
				{ content: 'Sounds like a plan!', sender: 'You', time: '15:20' }
			]
		},
		{
			chat_id: 20200303,
			username: 'Lily',
			timestamp: '21:44',
			message_head: 'i want to meet.',
			messages: [
				{ content: 'Hey, long time no see!', sender: 'Lily', time: '21:30' },
				{ content: 'Yeah! Let’s meet up soon.', sender: 'You', time: '21:35' },
				{ content: 'I want to meet tomorrow if you’re free.', sender: 'Lily', time: '21:44' }
			]
		},
		{
			chat_id: 20230303,
			username: 'Dumass',
			timestamp: '21:45',
			message_head: 'man this is boring.',
			messages: [
				{ content: 'Dude, I’m so bored.', sender: 'Dumass', time: '21:40' },
				{ content: 'Same here, nothing exciting happening.', sender: 'You', time: '21:42' },
				{ content: 'Man, this is boring.', sender: 'Dumass', time: '21:45' }
			]
		},
		{
			chat_id: 20270123,
			username: 'Baka',
			timestamp: '15:12',
			message_head: 'bro can i-',
			messages: [
				{ content: 'Bro, can I borrow your charger?', sender: 'Johnny Boi', time: '15:10' },
				{ content: 'Sure, I’ll bring it over.', sender: 'You', time: '15:11' },
				{ content: 'Actually, nvm it’s nothing.', sender: 'Johnny Boi', time: '15:12' }
			]
		},
		{
			chat_id: 20272303,
			username: 'Kawaii',
			timestamp: '15:12',
			message_head: 'bro can i-',
			messages: [
				{ content: 'Bro, can I borrow your charger?', sender: 'Johnny Boi', time: '15:10' },
				{ content: 'Sure, I’ll bring it over.', sender: 'You', time: '15:11' },
				{ content: 'Actually, nvm it’s nothing.', sender: 'Johnny Boi', time: '15:12' }
			]
		},
		{
			chat_id: 2027423,
			username: '<3',
			timestamp: '15:12',
			message_head: 'bro can i-',
			messages: [
				{ content: 'Bro, can I borrow your charger?', sender: 'Johnny Boi', time: '15:10' },
				{ content: 'Sure, I’ll bring it over.', sender: 'You', time: '15:11' },
				{ content: 'Actually, nvm it’s nothing.', sender: 'Johnny Boi', time: '15:12' }
			]
		}
	];
</script>

<main class="bg-background flex min-h-screen min-w-screen flex-row">
	<!-- sidebar -->
	<Sidebar {username} {invite_code} {user_data} />
	<!-- chat section -->
	{#if $activeChat != -1}
		<ChatWindow {user_data} active_chat={$activeChat} />
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
