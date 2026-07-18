from enum import Enum


class LanguageFormClass(str, Enum):
    RECONSTRUCTED = "reconstructed"
    PLAUSIBLE = "plausible"
    CURVATURE_DERIVED = "curvature-derived"
    FICTIONAL = "fictional"
    UNCERTAIN = "uncertain"


class ConfidenceLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"
