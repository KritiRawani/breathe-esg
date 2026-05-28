from emissions.models import EmissionRecord
from audit.models import AuditLog


def approve_record(record_id, reviewed_by):

    record = EmissionRecord.objects.get(id=record_id)

    old_status = record.status

    record.status = 'APPROVED'
    record.save()

    AuditLog.objects.create(
        emission_record=record,
        action='APPROVED',
        changed_by=reviewed_by,
        old_value=old_status,
        new_value='APPROVED'
    )

    return record


def reject_record(record_id, reviewed_by):

    record = EmissionRecord.objects.get(id=record_id)

    old_status = record.status

    record.status = 'REJECTED'
    record.save()

    AuditLog.objects.create(
        emission_record=record,
        action='REJECTED',
        changed_by=reviewed_by,
        old_value=old_status,
        new_value='REJECTED'
    )

    return record


def lock_record(record_id, reviewed_by):

    record = EmissionRecord.objects.get(id=record_id)

    old_status = record.status

    record.status = 'LOCKED'
    record.save()

    AuditLog.objects.create(
        emission_record=record,
        action='LOCKED',
        changed_by=reviewed_by,
        old_value=old_status,
        new_value='LOCKED'
    )

    return record