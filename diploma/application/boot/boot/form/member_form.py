from pweb import PWebForm, fields


class MemberForm(PWebForm):
    firstname = fields.String(required=True, error_messages={"required": "Please enter firstname"})
    lastname = fields.String(allow_none=True)
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")
    dob = fields.Date(required=True, error_messages={"required": "Please enter date of birth"})
