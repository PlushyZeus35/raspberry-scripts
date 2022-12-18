var nodemailer = require('nodemailer');
const fs = require('fs');
const path = require('path');
const config = require('../config');
const { promisify } = require('util');
const EmailCtrl = {};

// email sender function
EmailCtrl.sendEmail = async function(receiver,subject='PlushyApp Message Info',message='',attachments=[]){
    // Definimos el transporter
    var transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: 'borja.lorenzo.adm@gmail.com',
            pass: config.email.password    // Contraseña de aplicación en ajustes de Google
        }
    });
    // Definimos el email
    var mailOptions = {
        from: 'borja.lorenzo.adm@gmail.com',
        to: receiver,
        subject: subject,
        text: message,
        attachments: []
    };
    for(let i=0; i<attachments.length; i++){
        mailOptions.attachments.push(attachments[i]);
    }
    // Enviamos el email
    transporter.sendMail(mailOptions, function(error, info){
        if (error){
            console.log(error);
            return false;
        } else {
            console.log("Email sent");
            return true;
        }
    });
};

EmailCtrl.sendHTML = async function(receiver,subject='PlushyApp Message Info',html='',attachments=[]){
    // Definimos el transporter
    var transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: 'borja.lorenzo.adm@gmail.com',
            pass: 'drizilloijnvrylo'    // Contraseña de aplicación en ajustes de Google
        }
    });
    // Definimos el email
    var mailOptions = {
        from: 'borja.lorenzo.adm@gmail.com',
        to: receiver,
        subject: subject,
        html: html,
        attachments: []
    };
    for(let i=0; i<attachments.length; i++){
        mailOptions.attachments.push(attachments[i]);
    }
    // Enviamos el email
    transporter.sendMail(mailOptions, function(error, info){
        if (error){
            console.log(error);
            return false;
        } else {
            console.log("Email sent");
            return true;
        }
    });
};

EmailCtrl.sendErrorMail = async function(subject='', error='', message='', extraAttachments=[]){
    const mainAttachments = [{filename: 'Logo.png', path: path.join(__dirname, '../static/img/zeus.png'),cid: 'logo'},{filename: 'Bug.png', path: path.join(__dirname, '../static/img/bug.png'),cid: 'bug'}];
    const attachments = mainAttachments.concat(extraAttachments);
    fs.readFile(path.join(__dirname, '../email/error.html'), 'utf-8', function(err,data) {
        if(!err){
            data = data.replace('{{script}}', error);
            data = data.replace('{{scriptError}}', message);
            EmailCtrl.sendHTML(config.email.receiver,subject , data, attachments);
        }else{
            console.log(err)
        }
    })
}

module.exports = EmailCtrl;