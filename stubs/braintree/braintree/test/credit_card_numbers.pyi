class CreditCardNumbers:
    class CardTypeIndicators:
        Commercial: str
        DurbinRegulated: str
        Debit: str
        Healthcare: str
        Payroll: str
        Prepaid: str
        IssuingBank: str
        CountryOfIssuance: str
        No: str
        Unknown: str

    Maestro: str
    MasterCard: str
    MasterCardInternational: str
    Visa: str
    VisaInternational: str
    VisaPrepaid: str
    Discover: str
    Elo: str
    Hiper: str
    Hipercard: str
    Amex: str

    class FailsSandboxVerification:
        AmEx: str
        Discover: str
        MasterCard: str
        Visa: str

    class AmexPayWithPoints:
        Success: str
        IneligibleCard: str
        InsufficientPoints: str

    class Disputes:
        Chargeback: str
