from typing import Final

class AuthenticationIds:
    ThreeDSecureVisaFullAuthentication: Final = "fake-three-d-secure-visa-full-authentication-id"
    ThreeDSecureVisaLookupTimeout: Final = "fake-three-d-secure-visa-lookup-timeout-id"
    ThreeDSecureVisaFailedSignature: Final = "fake-three-d-secure-visa-failed-signature-id"
    ThreeDSecureVisaFailedAuthentication: Final = "fake-three-d-secure-visa-failed-authentication-id"
    ThreeDSecureVisaAttemptsNonParticipating: Final = "fake-three-d-secure-visa-attempts-non-participating-id"  # noqa: Y053
    ThreeDSecureVisaNoteEnrolled: Final = "fake-three-d-secure-visa-not-enrolled-id"
    ThreeDSecureVisaUnavailable: Final = "fake-three-d-secure-visa-unavailable-id"
    ThreeDSecureVisaMPILookupError: Final = "fake-three-d-secure-visa-mpi-lookup-error-id"
    ThreeDSecureVisaMPIAuthenticateError: Final = "fake-three-d-secure-visa-mpi-authenticate-error-id"
    ThreeDSecureVisaAuthenticationUnavailable: Final = "fake-three-d-secure-visa-authentication-unavailable-id"  # noqa: Y053
    ThreeDSecureVisaBypassedAuthentication: Final = "fake-three-d-secure-visa-bypassed-authentication-id"  # noqa: Y053
    ThreeDSecureTwoVisaSuccessfulFrictionlessAuthentication: Final = (
        "fake-three-d-secure-two-visa-successful-frictionless-authentication-id"  # noqa: Y053
    )
    ThreeDSecureTwoVisaSuccessfulStepUpAuthentication: Final = (
        "fake-three-d-secure-two-visa-successful-step-up-authentication-id"  # noqa: Y053
    )
    ThreeDSecureTwoVisaErrorOnLookup: Final = "fake-three-d-secure-two-visa-error-on-lookup-id"
    ThreeDSecureTwoVisaTimeoutOnLookup: Final = "fake-three-d-secure-two-visa-timeout-on-lookup-id"
