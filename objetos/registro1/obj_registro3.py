from objetos.funciones import base, sendPostHeaders

def registro3(headers):
    try:
        url = base + 'user/permissions/register-list'
        myBody = [
            {
                "status": True,
                "permissionType": "NOTIFICATION_PROCESS"
            },
            {
                "status": True,
                "permissionType": "REMINDER"
            },
            {
                "status": True,
                "permissionType": "RECOMMENDATIONS"
            },
            {
                "status": True,
                "permissionType": "NEWSLETTER_INTERNAL"
            },
            {
                "status": True,
                "permissionType": "NEWSLETTER_EXTERNAL"
            }
        ]
        sendPostHeaders(url, headers, myBody, 200)
        print("se manda las notificaciones")
        return 'se mandan las notificaciones'
    except Exception as e:
        print('No se mandaron las notificaiones', {e})
        return 'No se mandaron las notificaiones'

