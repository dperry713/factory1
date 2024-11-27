from flask import jsonify

def paginate_query(query, page, per_page):
    paginated_query = query.paginate(page=page, per_page=per_page, error_out=False)
    return {
        "items": [item.to_dict() for item in paginated_query.items],
        "total": paginated_query.total,
        "page": paginated_query.page,
        "pages": paginated_query.pages,
    }
