battery_drain_per_mine = 15
profit_target = 100

def mine_asteroid(size, scan_clearance=False):
    # No input() inside here! Use the parameters provided.
    if scan_clearance == True:
        minerals = size * 2
    else:
        if size > 5:
            minerals = size * 1.5
        else:
            minerals = 0
    return minerals

def process_and_sell(minerals):
    if minerals > 20:
        profit = minerals * 3
    else:
        profit = minerals * 2
    return profit

total_profit = 0
drone_battery = 100

while True:
    print(f"\n--- Status: Profit = {total_profit}/{profit_target} | Battery = {drone_battery}% ---")
    choice = input("Enter command (mine/quit): ").strip().lower()
    
    if choice == "quit":
        print("Exiting simulator. Goodbye!")
        break
    elif choice != "mine":
        # If they type anything else, pass and restart the loop
        print("Unknown system command.")
        pass
    else:
        # Gather inputs in the main execution block
        asteroid_size = int(input("Enter asteroid size (1-10): "))
        clearance_input = input("Clearance code? (True/False): ")
        
        # Proper boolean check
        clearance = (clearance_input == "True")
        
        # Deduct battery
        drone_battery -= battery_drain_per_mine
        
        # CONNECTING THE PIPELINE:
        # 1. Mine the asteroid and store returned minerals
        minerals_gathered = mine_asteroid(asteroid_size, clearance)
        
        # 2. Pass minerals to refinery and store returned profit
        round_profit = process_and_sell(minerals_gathered)
        
        # 3. Add to global tracker
        total_profit += round_profit
        print(f"Mined {minerals_gathered} minerals. Earned {round_profit} credits!")
        
    # GAME OVER CHECKS
    if total_profit >= profit_target:
        print("\n🏆 Victory! Profit target met! You are a master prospector.")
        break
    if drone_battery <= 0:
        print("\n💀 System Crash! Battery depleted in deep space.")
        break
