# Write a function that takes 1 parameter, a list of months.
# In the function create a new empty list and append an abbreviated version of each month
# to the new list i.e. ["Jan", "Feb" etc]
def short(mon):
    return [mon[i][0:3]for i in range(len(mon))]


def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    catch = short(months)
    print(catch)


if __name__ == '__main__':
    main()

