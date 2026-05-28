import pandas as pd

from .models import DataSource, RawRecord
from tenants.models import Tenant


def process_sap_csv(file, uploaded_by):

    df = pd.read_csv(file)

    tenant = Tenant.objects.first()

    data_source = DataSource.objects.create(
        tenant=tenant,
        source_type='SAP',
        uploaded_file_name=file.name,
        uploaded_by=uploaded_by
    )

    for _, row in df.iterrows():

        RawRecord.objects.create(
            data_source=data_source,
            raw_data=row.to_dict(),
            processing_status='PROCESSED'
        )

    return data_source