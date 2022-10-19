# Find_Sanitize_Flask_SQL_Alchemy

# Example of combining Flask-Security and Flask-Admin.
# by Steve Saporta
# April 15, 2014
#
# Uses Flask-Security to control access to the application, with "admin" and "end-user" roles.
# Uses Flask-Admin to provide an admin UI for the lists of users and roles.
# SQLAlchemy ORM, Flask-Mail and WTForms are used in supporting roles, as well.

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import current_user, login_required, RoleMixin, Security, \
    SQLAlchemyUserDatastore, UserMixin, utils
from flask_mail import Mail
from flask.ext.admin import Admin
from flask.ext.admin.contrib import sqla

from wtforms.fields import PasswordField

# Initialize Flask and set some config values
app = Flask(__name__)
app.config['DEBUG']=True
# Replace this with your own secret key
app.config['SECRET_KEY'] = 'super-secret'
# -------------------------------------------------

# scenario 1 - Simple query
db.session.query(sonething)
# scenario 2 - Query + filter
db.session.query(sonething).filter(field)
# scenario 3 - Just filter
db.session.filter(field)

# scenario 4 - Query with join 
db.session.query(Adjustment, Campaign)
                .join(
                    Campaign,
                    and_(
                        Campaign.oms_campaign_id == Adjustment.oms_campaign_id,
                        Campaign.yyyymm == Adjustment.payment_period,
                    ),
                )
                
# scenario 5 - Query with join and filter
db.session.query(Adjustment, Campaign)
                .join(
                    Campaign,
                    and_(
                        Campaign.oms_campaign_id == Adjustment.oms_campaign_id,
                        Campaign.yyyymm == Adjustment.payment_period,
                    ),
                )                
                .filter(Adjustment.id == adjustment_id)
                
# scenario 6 - query with distinct           
db.session.query(AuditLog.line_item_name, AuditLog.description, AuditLog.field)
            .distinct()
            .filter(AuditLog.oms_campaign_id == oms_campaign_id)
            .all()              
            
# scenario 7 - query with all           
db.session.query(AuditLog.line_item_name, AuditLog.description, AuditLog.field)            
            .all()              

# scenario 8 - query with distinct           
db.session.query(AuditLog.line_item_name, AuditLog.description, AuditLog.field)
            .distinct()

# scenario 9 - query with all and filter           
db.session.query(AuditLog.line_item_name, AuditLog.description, AuditLog.field)
            .all()     
            .filter(AuditLog.oms_campaign_id == oms_campaign_id)
            

# scenario 9 - query with filter and all           
db.session.query(AuditLog.line_item_name, AuditLog.description, AuditLog.field)            
            .filter(AuditLog.oms_campaign_id == oms_campaign_id)
            .all()                 
            
# scenario 9 - query with distinct and filter
db.session.query(AuditLog.line_item_name, AuditLog.description, AuditLog.field)
            .distinct()
            .filter(AuditLog.oms_campaign_id == oms_campaign_id)
            
# scenario 9 - query with distinct   and all
db.session.query(AuditLog.line_item_name, AuditLog.description, AuditLog.field)
            .distinct()
            .all()                 

# scenario 13 - Query and filter and one
db.session.query(LineItem.adjusted_audited_impressions, LineItem.adjusted_audited_revenue)
            .filter_by(oms_line_item_id=adjustment_line_data.oms_line_item_id, yyyymm=adjustment_line_data.yyyymm)
            .one()

# scenario 14 - Query and join and filter            
db.session.query(Adjustment, Campaign)
                .join(
                    Campaign,
                    and_(
                        Campaign.oms_campaign_id == Adjustment.oms_campaign_id,
                        Campaign.yyyymm == Adjustment.payment_period,
                    ),
                )
                .filter(Adjustment.id == adjustment_id)        
                
# scenario 15 - Query not in db.session
adjustment_query = adjustment_query.options(
                Load(Adjustment).load_only(*adjustment_fields),  # type: ignore[attr-defined]
            )

# scenario 16 - Query and filter and one not in db.session
AuditLog.query.filter_by(oms_campaign_id=order.oms_campaign_id).one()
     
     
# scenario 17 - Query and filter and one not in db.session     
dimension_param_list = (
            WorkbookParams.query.filter_by(workbook_id=workbook_id, param_section="dimension")
            .order_by(WorkbookParams.param_key)
            .all()
)
        
# scenario 18 - Query and filter and one not in db.session        
sync_required_available = db.session.query(query.filter(Campaign.sync_required.is_(True)).exists()).scalar()

# scenario 19 - add           
db.session.add(
            AuditLog(
                oms_campaign_id=line_item_dto.oms_campaign_id,
                oms_line_item_id=line_item.oms_line_item_id,
                description=AuditLogDescription.MANUAL_EDIT,
                field="review_status",
                line_item_name=line_item.line_item_name,
                previous_value="Reviewed" if line_item.review_status else "Not Reviewed",
                current_value="Reviewed" if line_item_dto.review_status else "Not Reviewed",
                updated_by=updated_by,
                updated_at=datetime.now(),
            )
        )        

# scenario 20 - Query and filter and one not in db.session
WorkbookContentPartner.query.filter()

# scenario 21 - Queryexecute and commit
sql_queries = dump_file.read()
db.session.execute(text(sql_queries)) #unsafe
db.session.commit()
            
            
from sqlalchemy.sql import text

# scenario 22 - Query from_statement
user = session.query(User).from_statement(
    text("""SELECT * FROM users where name=:name""")
).params(name="ed").all()


# scenario 22 - Query from_statement string literal -- SAFE
user = session.query(User).from_statement(
    text("""SELECT * FROM users where name='John'""")
).all()


# scenario 23 - Query +  filterby + from_statement
user = session.query(User).filter_by(name="john").from_statement(
    text("""SELECT * FROM users where name=:name""")
).params(name="ed").all()


# scenario 24 - Query +  filterby with expression + from_statement
user = session.query(User).filter_by(name=" \" or 1=1 ").from_statement(
    text("""SELECT * FROM users where name=:name""")
).params(name="ed").all()

result = connection.execute(text("SELECT * FROM users"))
