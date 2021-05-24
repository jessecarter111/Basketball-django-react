class utils {
    //change birth_date in django to '09-19-1999' format
    calc_age(birth_date) {
        //Player birth_date of the form "September 19, 1999"
        formattedBirthDate = birth_date.replace(/,/g, '').split(' ')
        formattedBirthDate[0] = MonthsToNumerical[formattedBirthDate[0]]
        currDate = new Date()

    }
}

const MonthsToNumerical = {
    January: 1,
    February: 2,
    March: 3, 
    April: 4,
    May: 5,
    June: 6,
    July: 7,
    August: 8, 
    September: 9,
    October: 10,
    November: 11,
    December: 12
}