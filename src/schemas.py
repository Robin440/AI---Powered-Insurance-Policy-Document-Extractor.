from datetime import date
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict


class Evidence(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_name: str = Field(min_length=1)
    quote: str = Field(min_length=1, description="Exact supporting text copied from the policy")
    page_number: int | None = Field(default=None, ge=1)


class PersonDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")
    full_name: str | None = None
    date_of_birth: date | None = None
    address: str | None = None


class PremiumDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")
    amount: float | None = Field(default=None, ge=0)
    currency: str | None = None
    payment_frequency: Literal[
        "monthly", "quarterly", "half_yearly", "yearly", "single", "unknown"
    ] = "unknown"
    tax_amount: float | None = Field(default=None, ge=0)


class CoverageItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    description: str | None = None
    limit_amount: float | None = Field(default=None, ge=0)
    limit_currency: str | None = None


class WaitingPeriod(BaseModel):
    model_config = ConfigDict(extra="forbid")
    condition: str
    duration: str | None = None
    details: str | None = None


class InsurancePolicyExtraction(BaseModel):
    """Structured facts extracted from an insurance policy. Unknown facts must be None."""
    model_config = ConfigDict(extra="forbid")

    document_type: Literal[
        "health", "life", "motor", "travel", "home", "other", "unknown"
    ] = "unknown"
    insurer_name: str | None = None
    product_name: str | None = None
    policy_number: str | None = None
    uin: str | None = None
    policyholder: PersonDetails = Field(default_factory=PersonDetails)
    insured_persons: list[PersonDetails] = Field(default_factory=list)
    policy_start_date: date | None = None
    policy_end_date: date | None = None
    premium: PremiumDetails = Field(default_factory=PremiumDetails)
    sum_insured: float | None = Field(default=None, ge=0)
    sum_insured_currency: str | None = None
    benefits: list[CoverageItem] = Field(default_factory=list)
    exclusions: list[str] = Field(default_factory=list)
    waiting_periods: list[WaitingPeriod] = Field(default_factory=list)
    riders: list[CoverageItem] = Field(default_factory=list)
    claim_process: list[str] = Field(default_factory=list)
    important_conditions: list[str] = Field(default_factory=list)
    missing_or_unclear_items: list[str] = Field(default_factory=list)
    evidence: list[Evidence] = Field(default_factory=list)
    extraction_notes: list[str] = Field(default_factory=list)
