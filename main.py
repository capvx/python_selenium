from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency(currency='EUR')
    bot.select_place_to_go('Novi Sad')
    bot.select_date(check_in_date='2022-08-17',
                    check_out_date='2022-08-25')
    bot.select_adults(30)
    bot.click_search()









