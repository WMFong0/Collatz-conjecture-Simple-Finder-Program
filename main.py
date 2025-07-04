from math import pow
import time

def collatz_conjecture(starting_power):
  result = {
    'max_steps': 0,
    'numbers_with_max_steps': [0],
    'current_max_found': False,
    'start_time': time.time()
  }

  start = 10**starting_power
  end = 10**(starting_power + 1)
  print(f"\n🔍 Analyzing Collatz sequences from 10^{starting_power} ({start:,}) to 10^{starting_power+1} ({end:,})")

  last_print_time = result['start_time']

  for num in range(start, end):
    x = num
    steps = 0

    while x != 1:
      if x % 2 == 0:
          x = x // 2
      else:
          x = x * 3 + 1
      steps += 1

    if ((time.time() - last_print_time)) >= 2 :
      print(f"⏱ Current number: {num:,}")
      last_print_time = time.time() + 2
      
    if steps > result['max_steps']:
      result['max_steps'] = steps
      result['numbers_with_max_steps'] = [num]
      result['current_max_found'] = True
      print(f"\n🎉 New record! {num:,} takes {steps:,} steps")
      last_print_time = time.time()
    elif steps == result['max_steps']:
      if len(result['numbers_with_max_steps']) < 10:
        result['numbers_with_max_steps'].append(num)
        print(f"\n➕ Found another: {num:,} also takes {steps:,} steps")
        last_print_time = time.time()

  return result

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

    total_time = time.time() - results['start_time']
    print("\n📊 Final Results:")
    print(f"Maximum steps found: {results['max_steps']:,}")
    print("Numbers with maximum steps:")
    for num in results['numbers_with_max_steps']:
      print(f"  - {num:,}")
    print(f"Total numbers with max steps: {len(results['numbers_with_max_steps'])}")
    hours, minutes, seconds = int(total_time // 3600), int((total_time // 60) % 60), total_time % 60
    if (hours != 0): print(f"Total computation time: {hours:02d}:{minutes:02d}:{seconds:06.3f}")
    else: print(f"Total computation time: {minutes:02d}:{seconds:06.3f}")

    if not results['current_max_found']:
      print("\nNote: No new maximum was found in this range.")

  except ValueError:
    print("Please enter a valid integer")
