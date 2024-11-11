from src.festival import festival, FESTIVAL_WESTERN, FESTIVAL_WINTER

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

def main():
		while True:
				print("\nMain Menu")
				print("1. Festival")
				print("2. Other")
				print("3. End")
				choice = input("Enter your choice: ").strip()

				if choice == '1':
						play_festival()
				elif choice == '2':
						print("Other functionality is not implemented yet.")
				elif choice == '3':
						print("Exiting the program. Goodbye!")
						break
				else:
						print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
		main()