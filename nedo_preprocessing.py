#есть блять
import pandas as pd
df_sotrudnik=pd.DataFrame(columns=['fio', 'location', 'grade'])
df_tasks=pd.DataFrame(columns=['name', 'priority', 'time_done', 'filter1', 'filter2', 'need_grade'])
df_points=pd.DataFrame(columns=['num', 'adress', 'has_materials','date_conn', 'date_after_issued', 'cnt_approved', 'cnt_issued'])

grade=['Синьор' 'Мидл', 'Джун']
filter={'Только синьор':'df_sotrudnik.loc[df_sotrudnik.grade=="Синьор"]',
'Синьор или мидл':'df_sotrudnik.loc[(df_sotrudnik.grade=="Синьор")|df_sotrudnik.grade=="Мидл"]',
'Все уровни':'df_sotrudnik.loc[(df_sotrudnik.grade=="Синьор")|(df_sotrudnik.grade=="Мидл")|{df_sotrudnik.grade=="Джун"]'}
priority={'Высокий':0.74, 'Средний':1, 'Низкий':1.25}
tasks=['1', '2', '3', '4', '5']
time_complite=[1,2, 1.5, 4]
time_drive_to_point=[1.1, 0.5, 2, 1]

filter1={'Дата выдачи последней карты более 7 дней назад, при этом есть одобренные заявки':'(df_points.date_after_issued>7) and (df_points.cnt_approved>0)',
        'Отношение кол-ва выданных карт к одобренным заявкам менее 50%, если выдано больше 0 карт':'(df_points.cnt_issued>0) and (df_points.cnt_approved>==issued*2)',
      'Точка подключена вчера':'df_points.date_conn=="Вчера"', 'Дата выдачи последней карты более 14 дней назад':'df_points.date_after_issued>14',
         'Карты и материалы не доставлялись':"df_points.has_materials=='Нет'"}
filter2={'Дата выдачи последней карты более 7 дней назад, при этом есть одобренные заявки':'(df_points.date_after_issued>7) and (df_points.cnt_approved>0)',
        'Отношение кол-ва выданных карт к одобренным заявкам менее 50%, если выдано больше 0 карт':'(df_points.cnt_issued>0) and (df_points.cnt_approved>==issued*2)',
      'Точка подключена вчера':'df_points.date_conn=="Вчера"'}
df_tasks.merge(df_sotrudnik, left_on='need_grade', right_on=filter(df_tasks.need_grade).valus(), how='left')


df_tasks.merge(df_sotrudnik, left_on='need_grade', right_on=filter('need_grade'), how='left')

#
#df_tasks merge df_point on filters.value merge df_sotrudnik on grade надеюсь тут хотя бы идея понятна

res = []






