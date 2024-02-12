labels_mapping = default_dict(default=list)
for row in initial_db:
    label = getLabel(type,secType,SecID)
    labels_mapping[label].append([type, secType, SecID])


for row in import_results:
    label_variants = labels_mapping[row.label]
    for variant in label_variants:
        write_db(
            type=variant[0],
            secType=variant[1],
            secId=variant[2],
            date=row.date,
            price=row.price,
            imported_status=row.imported_status,
        )
