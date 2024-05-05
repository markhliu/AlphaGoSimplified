# AlphaGo Simplified: Ruled-Based A.I. and Deep Learning in Everyday Games
<hr width="100%">
<i><b>The whole is greater than the sum of its parts.</b> -- Aristotle</i>
<hr width="100%">

<img src="https://gattonweb.uky.edu/faculty/lium/go.jpg" width="463" height="678">

May 11, 1997, was a watershed moment in the history of artificial intelligence (AI): the IBM supercomputer Chess engine, Deep Blue, beat the world Chess champion, Garry Kasparov. It was the first time a machine had triumphed over a human player in a Chess tournament. The news garnered much media attention. But here's the twist: Deep Blue was no machine learning (ML) marvel; it was powered by traditional rule-based AI, a far cry from the modern AI we know today.

Fast forward 19 years to the electrifying showdown of 2016, where Google DeepMind's AlphaGo took on Go champion Lee Sedol. Once again, AI seized the spotlight, creating a frenzy in the media. But this time, it was a new kind of AI, driven by the incredible force of ML, particularly deep reinforcement learning, that captured the world's imagination. The strategies it employed were a game-changer, quite literally. But that's not all! The real secret to AlphaGo’s success is the fact that it merged deep reinforcement learning with rule-based AI such as Monte Carlo Tree Search (MCTS) to supercharge the game strategies (the whole is indeed greater than the sum of its parts in this case).

Now, you may be wondering: What is ML, and how does it relate to AI? Why is deep learning all the rage in today's tech-driven world? This book has the answers. In these pages, you'll unravel the inner workings of traditional rule-based AI and modern ML. I'll show you how to apply these concepts to three simple yet captivating games: Last Coin Standing, Tic Tac Toe, and Connect Four. You'll dive into the exciting world of artificial intelligence through the thrilling stories of Deep Blue and AlphaGo, two groundbreaking moments that rewrote the history of AI.

For readers who are unfamiliar with these games, Last Coin Standing (the coin game from now on) is a game in which two players take turns removing one or two coins at a time from a pile of 21 coins. The player who takes the last coin is the winner. In Tic Tac Toe, two players take turns marking a cell with an X or O in a three-by-three grid. The first player to connect three Xs or Os in a row horizontally, vertically, or diagonally wins. Connect Four pits two players against each other in a quest to form a direct line of four game pieces of the same color.

Why these three games, you ask? Well, they're simple to grasp and perfect for exploring the world of rule-based AI, deep reinforcement learning (e.g., policy gradients or the actor-critic method), and other AI techniques. There is no need for you to get bogged down in complex game rules. In contrast, games like Chess and Go require a deep well of domain knowledge to devise effective strategies. Deep Blue's algorithm, for instance, uses thousands of rules to evaluate board positions in Chess. The game of Go involves complicated rules like “no self-capturing”, “komi” (compensation for the first mover's advantage), and the tricky concept of "ko" (avoiding creating a previous board position). What's more, applying rule-based AI and deep learning to these three games is fast and easy and doesn't require costly computational resources. As you'll discover in this book, you can train intelligent game strategies on a regular computer in minutes or hours. As a result, the trained AI provides perfect solutions for the first two games, while Connect Four gets super-human performance. In contrast, Chess and Go require supercomputing facilities. Deep Blue blitzed through hundreds of millions of board positions each second, and AlphaGo gobbled up the processing power of 1920 CPUs and 280 GPUs. The average reader doesn't have access to such supercomputing might, which is why we choose everyday simple games to make AI learning accessible to everyone with a regular computer.

By immersing yourself in these three captivating games, you'll grasp the essence of rule-based AI, from the MiniMax algorithm to alpha-beta pruning and the exhilarating Monte Carlo Tree Search. Afterward, we'll venture into the realm of ML, specifically deep reinforcement learning – the secret sauce behind AlphaGo's victory. DeepMind's brilliant minds used the policy-gradient method and crafted two deep neural networks to train game strategies. You’ll learn how to combine modern ML techniques with rule-based AI to achieve superhuman performance, just like the DeepMind team did in the epic AlphaGo showdown. Get ready for an AI journey that's not just educational but downright thrilling!

This book is divided into four parts. Part I provides an introduction to the three games and outlines how to develop strategies using rule-based AI techniques like MiniMax and MCTS. Part II delves into deep learning and its application to the three games. Part III explores the fundamentals of reinforcement learning and demonstrates how to enhance game strategies through self-play deep reinforcement learning. Finally, in Part IV, we integrate rule-based AI with deep reinforcement learning to construct AlphaGo (and its successor, AlphaGo Zero) algorithms for the three games. 

Here’s an overview of the book:

<b>Part I: Rule-Based A.I.</b>

<b>Chapter 1: Rule-Based AI in the Coin Game</b>

In this chapter, we introduce the first of the three games featured in this book: the coin game. You'll be guided through the rules of the game and learn how to create a rule-based AI that can achieve a 100\% win rate against any opponent when playing in the second position.

<b>Chapter 2: Look-Ahead Search in Tic Tac Toe</b> 

you'll delve into the rules of the second game: Tic Tac Toe. You'll learn how to develop strategies that enable the AI to plan up to three moves ahead. To think one step ahead, the AI evaluates all possible next moves to see if any of them immediately result in a win. If so, the AI takes that move. Thinking two steps ahead involves the AI trying to block the opponent from winning in their next turn. By thinking three steps ahead, the AI chooses the path that is most likely to lead to victory after three moves. In many cases, thinking three steps ahead ensures that the AI can secure a win within three moves.

<b>Chapter 3: Planning Three Steps Ahead in Connect Four</b>

In this chapter, you'll learn how to play Connect Four in the local game environment and develop rule-based AI strategies for the game. These AI players will think up to three moves ahead. When the AI looks one step ahead, it evaluates all possible next moves and chooses one that could lead to an immediate win. However, thinking two steps ahead in Connect Four introduces more complexity. The AI must determine whether its next move will block the opponent's win or inadvertently help them win. Our strategy for this scenario is twofold: if the AI's move blocks the opponent, it proceeds with that move; otherwise, it avoids a move that helps the opponent win in two moves. When thinking three steps ahead, the AI follows the path that is most likely to lead to victory after three moves. 

<b>Chapter 4: Recursion and MiniMax Tree Search</b>

Up to this point, you have been hardcoding look-ahead search techniques to devise game strategies. However, extending this approach beyond three steps becomes increasingly cumbersome and prone to errors. To address this, you'll learn a more efficient method for conducting look-ahead searches: the MiniMax tree search. You'll learn how to implement the MiniMax tree search in the coin game by employing recursion, which involves calling a function within itself. This recursive approach enables the MiniMax agent to search ahead until the end of the game. As a result, the MiniMax agent is able to solve the coin game.

<b>Chapter 5: Depth Pruning in MiniMax</b>

You'll begin by developing a MiniMax agent for Tic Tac Toe using recursion. The MiniMax tree search method explores all potential future paths and solves the game. However, in more complex games like Connect Four, Chess, or Go, the MiniMax algorithm is unable to exhaustively explore all possible future paths in a reasonable time. To overcome this limitation, the algorithm employs a technique called depth pruning. This approach involves searching a specific number of moves ahead and then stopping the search. You'll learn how to create a MiniMax agent with depth pruning and apply it to Connect Four.

<b>Chapter 6: Alpha-Beta Pruning</b>

Alpha-beta pruning enhances the look-ahead search algorithm by allowing it to bypass branches that cannot impact the final outcome of the game. This optimization significantly reduces the time it takes for the MiniMax agent to decide on a move, enabling it to explore more steps ahead and develop smarter moves within a given time frame. To apply alpha-beta pruning in a game, the agent keeps track of two values: alpha and beta, which represent the best possible outcomes for the two players, respectively. Whenever $alpha>−beta$, or equivalently $beta>−alpha$, the agent stops searching a branch. You'll implement alpha-beta pruning in both Tic Tac Toe and Connect Four. By incorporating this technique, the time required for the MiniMax agent to decide on a move is reduced by up to 97\%, making the algorithm much more efficient.

<b>Chapter 7: Position Evaluation in MiniMax</b>

Depth pruning enables a MiniMax agent to develop intelligent (though not perfect) strategies quickly in complex games. In earlier chapters, when the depth of a tree search reaches zero and the game is not yet over, the algorithm assumes a tied game. However, in many real-world games, we often have a good estimate of the outcome based on heuristics, even when the game is not over. In this chapter, you'll learn the concept of the position evaluation function and apply it to the Connect Four game. When the depth reaches zero in a tree search and the game is not over, you'll use an evaluation function to assess the value of the game state. This evaluation function provides a more accurate assessment of the game state, enabling the MiniMax agent to make more intelligent moves.

<b>Chapter 8: Monte Carlo Tree Search</b>

MiniMax tree search, augmented by powerful position evaluation functions, helped Deep Blue beat the world Chess champion Garry Kasparov in 1997. While in games such as Chess, position evaluation functions are relatively accurate, in other games such as Go, evaluating positions is more challenging. In such scenarios, researchers usually use Monte Carlo Tree Search (MCTS). The idea behind MCTS is to roll out random games starting from the current game state and see what the average game outcome is. After rolling out, say 1000, games from this point, if Player 1 wins 99 percent of the time, the current game state must favor Player 1 over Player 2. To select the best next move, the MCTS algorithm uses the Upper Confidence Bounds for Trees (UCT) method. This chapter breaks down the process into four steps: selection, expansion, simulation, and backpropagation. Readers learn to implement a geneeric MCTS algorithm that can be applied to the three games in this book: the coin game, Tic Tac Toe, and Connect Four. 

<b>Part II: Deep Learning</b>

<b>Chapter 9: Deep Learning in the Coin Game</b>

In this chapter, you'll learn what deep learning is and how it's related to ML and AI. Deep learning is a type of ML method that's based on artificial neural networks. A neural network is a computational model inspired by the structure of neural networks in the human brain. It's designed to recognize patterns in data, and it contains layers of interconnected nodes, or neurons. You'll learn to use deep neural networks to design game strategies for the coin game in this chapter. In particular, you'll build and train two networks, a fast policy network and a strong policy network, to be used in the AlphaGo algorithm later in the book. 

<b>Chapter 10: Policy Networks in Tic Tac Toe</b>

In this chapter, you'll train a fast policy network and a strong policy network in Tic Tac Toe. The two networks contain convolutional layers, which treat game boards as multi-dimensional objects and extract spatial features from them. Convolutional layers greatly improve the predictive power of neural networks and this, in turn, leads to more intelligent game strategies. To generate expert moves in Tic Tac Toe, you'll use the MiniMax algorithm with alpha-beta pruning from Chapter 6. You’ll use game board positions as inputs and expert moves as targets to train the two policy neural networks. The two trained policy networks will be used in the AlphaGo algorithm later in this book.

<b>Chapter 11: A Policy Network in Connect Four</b>

In this chapter, you'll train a policy network in Connect Four so that it can be used in the AlphaGo algorithm later in the book. To generate expert moves, you'll first design an agent who chooses moves by using the MCTS algorithm half of the time and a MiniMax algorithm with alpha-beta pruning the other 50\% of the time. You let the above agent play against itself for 10,000 games. In each game, the winner's moves are considered expert moves while the loser's moves are discarded. You'll then create a deep neural network and use the self-play game experience data to train it to predict expert moves.

<b>Part III: Reinforcement Learning</b>

<b>Chapter 12: Tabular Q-Learning in the Coin Game</b>

You'll learn the basics of reinforcement learning in this chapter. You’ll use tabular Q-learning to solve the coin game. Along the way, you'll learn the concepts of dynamic programming and the Bellman equation. You'll also learn how to train and use Q-tables in tabular Q-learning.

<b>Chapter 13: Self-Play Deep Reinforcement Learning</b>

You'll learn to use self-play deep reinforcement learning to further train the strong policy network for the coin game. You'll learn what a policy is and how to implement the policy gradient method to train the agent in deep reinforcement learning. A policy is a decision rule that tells the agent what actions to take in a given game state. In the policy gradients method, the agent engages in numerous game sessions to learn the optimal policy. The agent bases its actions on the model's predictions, observes the resulting rewards, and adjusts the model parameters to align predicted action probabilities with desired probabilities. You'll also use the game experience data from self-plays to train a value network that predicts game outcomes based on current game states.

<b>Chapter 14: Vectorization to Speed Up Deep Reinforcement Learning</b>

You'll apply self-play deep reinforcement learning to Tic Tac Toe in this chapter. You'll learn to manage several challenges in the process. Firstly, unlike the coin game, where illegal moves are non-existent as players simply choose to remove one or two coins per turn, Tic Tac Toe has a decreasing number of legal moves as the game advances. You'll learn to assign negative rewards to illegal moves so the trained agent chooses only legal moves. Secondly, the computational demands of training for Tic Tac Toe are significantly higher than for the coin game. You'll learn to use vectorization to speed up the training process. Finally, this chapter will guide you through the process of encoding the game board in a player-independent manner so that the current player's game pieces are represented as 1 and the opponent's as $-1$. This allows the use of the same neural network for training both players. With the above challenges properly handled, you'll implement the policy gradient method in Tic Tac Toe to train a policy network. You'll also train a value network based on the game experience data.

<b>Chapter 15: A Value Network in Connect Four</b>

You'll apply the policy gradient method to Connect Four in this chapter. You'll learn to handle illegal moves by assigning a reward of $-1$ every time the agent makes an illegal move. You'll also use vectorization to speed up training. Self-play deep reinforcement learning is used to further train a policy network in Connect Four based on the policy network from Chapter 11. Readers also use the game experience data from self-play to train a value network: the network will predict the game outcome based on the board position.  

<b>Part IV: AlphaGo Algorithms</b>

<b>Chapter 16: Implementing AlphaGo in the Coin Game</b>

In this chapter, you'll implement the AlphaGo algorithm in the coin game. MCTS constitutes the backbone of AlphaGo's decision-making process: it is used to find the most promising moves by building a search tree. You'll learn to use three deep neural networks you developed in earlier chapters. The strengthened policy network (from Chapter 13) selects child nodes so that the most valuable child nodes are selected to roll out games. The fast policy network developed in Chapter 9 helps in narrowing down the selection of moves to consider in game rollouts. The value network from Chapter 13 evaluates board positions and predicts the winner of the game from that position so that the agent doesn't have to play out the entire game in rollouts. When moving second, the AlphaGo agent beats the ruled-based AI player in 100\% of games. 

<b>Chapter 17: AlphaGo in Tic Tac Toe and Connect Four</b>

In this chapter, you'll create an AlphaGo agent featuring two main enhancements. Firstly, it will be versatile and capable of handling two games, Tic Tac Toe and Connect Four. Secondly, the agent's game simulation strategy includes a choice between random moves and those suggested by a fast policy network. MCTS remains the core of the agent's decision process, involving selection, expansion, simulation, and backpropagation. Three deep neural networks, introduced in previous chapters, will enhance the tree search. You'll evaluate the AlphaGo algorithm's effectiveness in Tic Tac Toe. Against the perfect rule-based AI from Chapter 6, the AlphaGo agent consistently draws, indicating its ability to solve the game. 

<b>Chapter 18: Hyperparameter Tuning in AlphaGo</b>

Unlike agents in the coin game or Tic Tac Toe, the AlpahGo agent in Connect Four does not fully solve the game. This chapter, therefore, focuses on identifying the optimal combination of hyperparameters in AlphaGo that yields the most effective game strategy. Grid search is a common approach for hyperparameter tuning. This process involves experimenting with different permutations of hyperparameters in the model to determine empirically which combination offers the best performance. You'll learn to fine-tune four key hyperparameters for the AlphaGo agent in Connect Four in this chapter. The optimized AlphaGo agent can defeat an AI that plans four steps ahead.

<b>Chapter 19: The Actor-Critic Method and AlphaZero </b>

In 2017, the DeepMind team introduced an advanced version of AlphaGo, named AlphaGo Zero (which we'll refer to as AlphaZero in this book because we apply the algorithm to various games beyond Go). AlphaZero's training relied exclusively on deep reinforcement learning, without any human-derived strategies or domain-specific knowledge, except for the basic rules of the game. It learned through self-play from scratch. AlphaZero utilizes a single neural network with two outputs: a policy network for predicting the next move and a value network for forecasting game outcomes. In this chapter, you'll learn this advanced deep reinforcement learning strategy known as the actor-critic method, applying it specifically to the coin game. You'll then integrate both the policy and value networks from the actor-critic method with MCTS for making decisions in actual games, mirroring the approach used in the AlphaGo algorithm in Chapter 16. The AlphaZero agent developed in this chapter, if playing as Player 2, can beat the AlphaGo agent developed earlier in Chapter 16.

<b>Chapter 20: Iterative Self-Play and AlphaZero in Tic Tac Toe</b>

You'll learn to construct an AlphaZero agent for both Tic Tac Toe and Connect Four in this chapter. You'll then implement the AlphaZero algorithm in Tic Tac Toe by integrating a policy gradient network with MCTS. To train the model, you'll start a policy gradient network from scratch and initialize it with random weights. During training, the policy gradient agent competes against a more advanced version of itself: the AlphaZero agent. As training progresses, both agents gradually improve their performance. This dynamic scenario presents a unique challenge, as the agent effectively faces a moving target. To address this challenge, an iterative self-play approach is used. Initially, you'll keep the weights of the policy gradient network, as utilized by the AlphaZero agent, constant, while updating the weights within the policy gradient network itself. After an iteration of training, the weights in the policy gradient network used by the AlphaZero agent will be updated. This process is repeated in successive iterations until the AlphaZero agent perfects its gameplay.

<b>Chapter 21: AlphaZero in Unsolved Games</b>

In the previous two chapters, you have used rule-based AI to periodically evaluate the AlphaZero agent to gauge its performance and decide when to stop training. Even though rule-based AI was not used in the training process directly, it was used for testing purposes to monitor the agent's performance. In unsolved games, no game-solving algorithm can be used as the benchmark. How should we test the performance of AlphaZero and decide when to stop training in such cases? In this chapter, you'll treat Connect Four as an unsolved game. To test the performance of AlphaZero and decide when to stop training, an earlier version of AlphaZero is used as the benchmark. When AlphaZero outperforms an earlier version of itself by a certain margin, a training iteration is complete. You'll then update the parameters in the older version of AlphaZero and restart the training process. You'll train the AlphaZero model for several iterations so that the AlphaZero agent becomes increasingly stronger. The trained AlphaZero agent consistently outperforms its predecessor, AlphaGo, in Connect Four!

All Python programs, along with answers to some end-of-the-chapter questions, are
provided in the GitHub repository https://github.com/markhliu/AlphaGoSimplified.


