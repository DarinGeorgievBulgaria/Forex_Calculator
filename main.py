import customtkinter

currencyPair = ["AUD/CAD", "AUD/CHF", "AUD/JPY", "AUD/NZD", "AUD/USD",
                "CAD/CHF", "CAD/JPY",
                "CHF/JPY",
                "EUR/AUD", "EUR/CAD", "EUR/CHF", "EUR/GBP", "EUR/JPY", "EUR/NZD", "EUR/USD",
                "GBP/AUD", "GBP/CAD", "GBP/CHF", "GBP/JPY", "GBP/NZD", "GBP/USD",
                "NZD/CAD", "NZD/CHF", "NZD/JPY", "NZD/USD",
                "USD/CAD", "USD/CHF", "USD/JPY"]

accountCurrency = ["GBP", "EUR", "USD", "JPY", "CHF", "AUD", "CAD", "NZD"]
def positionSize():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("500x300")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Position Size Calculator", font=("Roboto", 20))
    label.pack(pady=12, padx=10)

    currencyPairMenuTop = customtkinter.StringVar(value=currencyPair[14])
    currencyPairMenu = customtkinter.CTkOptionMenu(master=frame, values=currencyPair, variable=currencyPairMenuTop)
    currencyPairMenu.pack()

    accountCurrencyMenuTop = customtkinter.StringVar(value=accountCurrency[0])
    accountCurrencyMenu = customtkinter.CTkOptionMenu(master=frame, values=accountCurrency, variable=accountCurrencyMenuTop)
    accountCurrencyMenu.pack(pady=7)

    entryAccountSize = customtkinter.CTkEntry(master=frame, placeholder_text="Account size:")
    entryAccountSize.pack()

    entryRiskRatio = customtkinter.CTkEntry(master=frame, placeholder_text="Risk ratio %:")
    entryRiskRatio.pack(pady=6)

    entryStopLoss = customtkinter.CTkEntry(master=frame, placeholder_text="Stop-Loss in pips:")
    entryStopLoss.pack(pady=6)

    root.mainloop()




if __name__ == "__main__":
    positionSize()
    print("The result is:")