import uuid

def generate_teacher_id():
    return str(uuid.uuid4())[:8]