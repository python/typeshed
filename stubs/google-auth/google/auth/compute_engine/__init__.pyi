from google.auth.compute_engine._metadata import detect_gce_residency_linux as detect_gce_residency_linux
from google.auth.compute_engine.credentials import Credentials as Credentials, IDTokenCredentials as IDTokenCredentials

__all__ = ["Credentials", "IDTokenCredentials", "detect_gce_residency_linux"]
