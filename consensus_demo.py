import random

# Simulate PoW
miners = {
    'MinerA': random.randint(10, 100),
    'MinerB': random.randint(10, 100),
    'MinerC': random.randint(10, 100)
}
pow_winner = max(miners, key=miners.get)
print("\n--- Proof of Work ---")
print("Miners:", miners)
print(f"Selected: {pow_winner} with power {miners[pow_winner]} (Highest computational power wins)")

# Simulate PoS
stakers = {
    'StakerA': random.randint(10, 100),
    'StakerB': random.randint(10, 100),
    'StakerC': random.randint(10, 100)
}
pos_winner = max(stakers, key=stakers.get)
print("\n--- Proof of Stake ---")
print("Stakers:", stakers)
print(f"Selected: {pos_winner} with stake {stakers[pos_winner]} (Highest stake wins)")

# Simulate DPoS
votes = {
    'DelegateA': random.randint(1, 100),
    'DelegateB': random.randint(1, 100),
    'DelegateC': random.randint(1, 100)
}
dpos_winner = max(votes, key=votes.get)
print("\n--- Delegated Proof of Stake ---")
print("Votes:", votes)
print(f"Selected: {dpos_winner} with {votes[dpos_winner]} votes (Most voted delegate wins)")
