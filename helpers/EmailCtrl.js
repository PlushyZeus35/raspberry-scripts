var nodemailer = require('nodemailer');
const fs = require('fs');
const { promisify } = require('util');
const readFile = promisify(fs.readFile);
const EmailCtrl = {};

// email sender function
EmailCtrl.sendEmail = async function(receiver,subject='PlushyApp Message Info',message='',attachments=[]){
    // Definimos el transporter
    var transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: 'borja.lorenzo.adm@gmail.com',
            pass: 'yphskrlkpaigreks'    // Contraseña de aplicación en ajustes de Google
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

module.exports = EmailCtrl;