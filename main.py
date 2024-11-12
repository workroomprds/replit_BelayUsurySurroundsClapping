from src.festival import FESTIVAL_WESTERN, FESTIVAL_WINTER, festival
from src.oddEven import oddEven
from src.fluvianNumerals import fluvianToArabic, arabicToFluvian

def play_festival():
    while True:
        try:
            year_input = input("Enter the year (or press Enter to exit): ").strip()
            if not year_input:  # Exit if the input is blank
                print("Exiting the festival calculation. Returning to main menu.")
                break

            year = int(year_input)
            print("Choose the festival type:")
            print(f"1. {FESTIVAL_WESTERN}")
            print(f"2. {FESTIVAL_WINTER}")
            festival_choice = input("Enter the number corresponding to the festival type: ")

            if festival_choice == '1':
                festival_type = FESTIVAL_WESTERN
            elif festival_choice == '2':
                festival_type = FESTIVAL_WINTER
            else:
                print("Invalid choice.")
                continue

            festival_date = festival(year, festival_type)
            print(f"The {festival_type} festival in {year} is on {festival_date}.")

        except ValueError as e:
            print(f"Error: {e}")

def play_odd_even():
  while True:
      try:
          number_input = input("Enter a number (or press Enter to exit): ").strip()
          if number_input == "":  # Exit if the input is blank
              print("Exiting the odd/even check. Returning to main menu.")
              break
          result = oddEven(number_input)
          print(f"The number {number_input} is {result}.")
      except ValueError as e:
          print(f"Error: {e}")

def play_fluvian_numerals():
  while True:
      try:
          print("\nFluvian Numerals Menu")
          print("1. Convert Fluvian to Arabic")
          print("2. Convert Arabic to Fluvian")
          print("3. Return to Main Menu")

          choice = input("Enter your choice: ").strip()

          if choice == '1':
              fluvian = input("Enter a Fluvian numeral: ").strip()
              arabic = fluvianToArabic(fluvian)
              print(f"The Arabic representation of {fluvian} is {arabic}.")
          elif choice == '2':
              arabic = int(input("Enter an Arabic number: ").strip())
              fluvian = arabicToFluvian(arabic)
              print(f"The Fluvian representation of {arabic} is {fluvian}.")
          elif choice == '3':
              print("Returning to main menu.")
              break
          else:
              print("Invalid choice. Please enter 1, 2, or 3.")
      except ValueError as e:
          print(f"Error: {e}")

def main():
  while True:
      print("\nMain Menu")
      print("1. Festival")
      print("2. Odd/Even Check")
      print("3. Fluvian Numerals Conversion")
      print("4. End")

      choice = input("Enter your choice: ").strip()
      if choice == '1':
          play_festival()
      elif choice == '2':
          play_odd_even()
      elif choice == '3':
          play_fluvian_numerals()
      elif choice == '4':
          print("Exiting the program. Goodbye!")
          break
      else:
          print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()