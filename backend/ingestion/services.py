import pandas as pd

from .models import DataSource, RawRecord

from tenants.models import Tenant

from emissions.models import EmissionRecord


def process_sap_csv(file, uploaded_by):

    df = pd.read_csv(file)

    tenant = Tenant.objects.first()

    if not tenant:

        tenant = Tenant.objects.create(
            name="Breathe ESG",
            industry="Technology"
        )

    data_source = DataSource.objects.create(
        tenant=tenant,
        source_type='SAP',
        uploaded_file_name=file.name,
        uploaded_by=uploaded_by
    )

    for _, row in df.iterrows():

        # SAVE RAW RECORD
        raw_record = RawRecord.objects.create(
            data_source=data_source,
            raw_data=row.to_dict(),
            processing_status='PROCESSED'
        )

        # CREATE EMISSION RECORD
        EmissionRecord.objects.create(

            tenant=tenant,

            source_record_id=str(raw_record.id),

            category=row.get("category", "General"),

            scope="Scope 1",

            activity_value=float(
                row.get("amount", 0)
            ),

            normalized_value=float(
                row.get("amount", 0)
            ),

            emission_kg_co2e=float(
                row.get("amount", 0)
            ),

            status="PENDING",

            is_suspicious=False
        )

    return data_source