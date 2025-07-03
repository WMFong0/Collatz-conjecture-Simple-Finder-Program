from math import pow

def collatz_conjecture(starting_power):
  result = {
    'max_steps': 0,
    'numbers_with_max_steps': [0],
    'current_max_found': False
  }
  
  start = 10**starting_power
  end = 10**(starting_power + 1)  
  number_count = 0
  print(f"\n🔍 Analyzing Collatz sequences from 10 ^{starting_power} ({start:,}) to 10 ^{starting_power+1} ({end:,})")

  for num in range(start, end):
    x = num
    steps = 0    
    if (num % 1000000 == 0):
      print(f"\n🔄Current Number is {num:,}")
      
    while x != 1:
      if x % 2 == 0:
        x = x // 2
      else:
        x = x * 3 + 1
      steps += 1

    if steps > result['max_steps']:
      result['max_steps'] = steps
      result['numbers_with_max_steps'] = [num]
      result['current_max_found'] = True
      print(f"🎉 New record! {num:,} takes {steps:,} steps")
    elif steps == result['max_steps']:
      if len(result['numbers_with_max_steps']) < 10:
        result['numbers_with_max_steps'].append(num)
        print(f"➕ Found another: {num:,} also takes {steps:,} steps")

  return result

# Main
print("Collatz Conjecture Maximum Steps Finder")
print("----------------------------------------")

while True:
  try:
    power = int(input("\nEnter starting power of 10 (or -1 to exit): "))

    if power == -1:
      print("Exit!")
      break
    elif power != 0 and power < 1:
      raise ValueError()
      continue
    
    results = collatz_conjecture(power)

    print("\n📊 Final Results:")
    print(f"Maximum steps found: {results['max_steps']:,}")
    print("Numbers with maximum steps:")
    for num in results['numbers_with_max_steps']:
      print(f"  - {num:,}")
    print(f"Total numbers with max steps: {len(results['numbers_with_max_steps'])}")

    if results['current_max_found'] == False:
        print("\nNote: No new maximum was found in this range.")
    
  except ValueError:
    print("Please enter a valid integer")
