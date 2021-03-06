from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError,TextAreaField,IntegerField, DateField,RadioField
from wtforms.validators import Length, Email, EqualTo, Required,URL,NumberRange
from jobplus.models import db, User,Company,Job
import re


class ApplicantRegisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(3,24)])
    email=StringField('邮箱地址',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    phone = StringField('电话',validators=[Required(),Length(3,24)])
    birthday = DateField('生日')
    gender = RadioField('性别', choices = [('1','男'), ('0','女')])

    submit=SubmitField('提交')

    def create_user(self):
        user=User()
        user.username=self.username.data
        user.email=self.email.data
        user.password=self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self,user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user
          

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已存在！')
        elif not bool(re.match('^[0-9a-zA-Z]+$',field.data)):
            raise ValidationError('用户名只能包含数字和大小写字母！')
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮件地址已存在！')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3, 24)])
    password = PasswordField('密码',validators=[Required(),Length(6,24)]    )
    
    submit = SubmitField('提交')


    def validate_username(self,field):
        if field.data and not User.query.filter_by(username=field.data).first():
            raise ValidationError('user not found')

    def valdiate_password(self,field):
        user=User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Password Error')


class CompanyRegisterForm(FlaskForm):
    name=StringField('公司名称',validators=[Required(),Length(1,32)])
    website_url = StringField('公司网址',validators=[Required(),URL()])
    location = StringField('公司地址',validators=[Required(),Length(1,128)])
    image_url = StringField('公司商标链接',validators=[Required(),URL()])
    description = TextAreaField('公司简介',validators=[Required(),Length(5,64)])
    submit = SubmitField('Submit')

'''
class CourseForm(FlaskForm):
    name=StringField('CourseName',validators=[Required(),Length(5,32)])
    description = TextAreaField('CourseDescription',validators=[Required(),Length(20,256)])
    image_url = StringField('CoverImage',validators=[Required(),URL()])
    author_id=IntegerField('AuthorID',validators=[Required(),NumberRange(min=1,message='InvalidUserID')])
    submit = SubmitField('Submit')

    def validate_author_id(self,field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('UserNotFound')

    def create_course(self):
        course=Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self,course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

class UserForm(FlaskForm):
    username = StringField('UserName',validators=[Required(),Length(3,24)])
    email=StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('RepeatPassword',validators=[Required(),EqualTo('password')])
    role=IntegerField('RolePrivilege',validators=[Required(),NumberRange(min=10,message=    'InvalidRoleID')])
    job=StringField('Job',validators=[Required(),Length(3,24)])
    submit=SubmitField('Submit')
    
    def create_user(self):
        user=User() 
        user.username=self.username.data
        user.email=self.email.data
        user.password=self.password.data
        user.role = self.role.data
        user.job=self.job.data
        db.session.add(user)
        db.session.commit()
        return user
    
    def update_user(self,user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user
 '''        


