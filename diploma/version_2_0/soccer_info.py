def soccer_info():
    print(f"В зависимости от ВЫБРАННОЙ НА МАТЧ ПОЗИЦИИ, игрок будет показывать силу, помноженную на модификатор флага/центра \n\
    Дополнительный фактор - НАСТРОЙ НА СЕЗОН. Условно обозначен в виде одной из мастей: ['♠', '♣', '♥', '♦'] \n\
Основной смысл масти раскрывается на стратегическом уровне, а в данном примере моделируется тактика на один сезон \n\
Если в линии (оборона, полузащита, атака по центру, левый фланг, правый фланг) несколько игроков одной масти, \n\
то сила каждого из них возрастает на 25% за каждого - т.е. если червовых игроков трое, то каждый играет сильнее на 75%. \n\
CM может получить бонусы и от полузащиты, и от атаки по центру \n\
        -------СОКРАЩЕНИЯ------- \n\
GK голкипер, вратарьn \n\
LD левый защитник \n\
SW свипер, последний защитник (всегда за спинами центральных, 'подчищает', с ним нельзя делать искусственный оффсайд) \n\
CD центральный защитник \n\
RD правый защитник \n\
DM (CD+CM) опорный полузащитник (оттягивается в оборону из центра поля, часто начинает свои атаки точными передачами) \n\
LM левый полузащитник \n\
CM центральный полузащитник \n\
RM правый полузащитник \n\
LW (LM+LF) левый вингер (по левой бровке подключается к атакам, навешивает с фланга) \n\
AM (CM+CF) центральный атакующий полузащитник, диспетчер (подключается к атакам из центра поля, отдаёт голевые передачи) \n\
RW (RM+RF) правый вингер (по правой бровке подключается к атакам, навешивает с фланга) \n\
LF левый форвард (врывается в штрафную с левого фланга) \n\
CF центрфорвард (атакует ворота по центру, замыкает навесы с флангов) \n\
RF правый форвард (врывается в штрафную с правого фланга) \n\
ST страйкер (действует только в атаке, завершает ударами в упор, назад почти не отходит, часто попадает в оффсайд) \n\
FR свободный художник (очень опытный игрок, которому позволено играть на своё усмотрение, обычно следует за мячом)")

if __name__ == '__main__':

    soccer_info()
