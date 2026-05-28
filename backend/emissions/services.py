from ingestion.models import RawRecord
from .models import EmissionRecord


EMISSION_FACTORS = {
    'Diesel': 2.68,
    'Petrol': 2.31,
    'Natural Gas': 1.90,
}


def normalize_unit(quantity, unit):

    if unit == 'Gallons':
        return quantity * 3.785, 'Liters'

    return quantity, unit


def detect_suspicious_record(quantity):

    if quantity > 10000:
        return True

    if quantity < 0:
        return True

    return False


def calculate_emissions():

    raw_records = RawRecord.objects.filter(
        processing_status='PROCESSED'
    )

    for raw in raw_records:

        data = raw.raw_data

        fuel_type = data.get('Fuel Type')

        quantity = float(data.get('Quantity'))

        unit = data.get('Unit')

        normalized_value, normalized_unit = normalize_unit(
            quantity,
            unit
        )

        emission_factor = EMISSION_FACTORS.get(
            fuel_type,
            1
        )

        emission_kg_co2e = normalized_value * emission_factor

        suspicious = detect_suspicious_record(
            normalized_value
        )

        status = 'FLAGGED' if suspicious else 'PENDING'

        EmissionRecord.objects.create(
            tenant=raw.data_source.tenant,

            source_record=raw,

            scope='Scope 1',

            category=fuel_type,

            activity_value=quantity,

            original_unit=unit,

            normalized_unit=normalized_unit,

            normalized_value=normalized_value,

            emission_kg_co2e=emission_kg_co2e,

            status=status,

            is_suspicious=suspicious
        )