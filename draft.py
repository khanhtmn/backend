                    if 'name' in request_data:
                        project_info.name = request_data['name']

                    if 'class_year' in request_data:
                        project_info.class_year = request_data['class_year']

                    if 'primary_major' in request_data:
                        project_info.primary_major = request_data['primary_major']                

                    if 'secondary_major' in request_data:
                        project_info.secondary_major = request_data['secondary_major']

                    if 'primary_concentration' in request_data:
                        project_info.primary_concentration = request_data['primary_concentration']

                    if 'secondary_concentration' in request_data:
                        project_info.secondary_concentration = request_data['secondary_concentration']                

                    if 'special_concentration' in request_data:
                        project_info.special_concentration = request_data['special_concentration']

                    if 'minor' in request_data:
                        project_info.minor = request_data['minor']

                    if 'minor_concentration' in request_data:
                        project_info.minor_concentration = request_data['minor_concentration']       




                name = None
                class_year = None
                primary_major = None
                secondary_major = None
                primary_concentration = None
                secondary_concentration = None
                special_concentration = None
                minor = None
                minor_concentration = None



query1 = self.session.query(ID_Streets, ID_Nps, ID_Streets_history, Modify_reason)\
            .join(ID_Nps, ID_Nps.id_np == ID_Streets.id_np)\
            .outerjoin(ID_Streets_history, text('(ID_Streets.id_np=ID_Streets_history.id_np '\
                'AND ID_Streets.id_street=ID_Streets_history.id_street)'))\
            .outerjoin(Modify_reason, text('(ID_Streets_history.code_reason=Modify_reason.code_reason '\
                'AND ID_Streets_history.code_detail=Modify_reason.code_detail)'))\
            .group_by(ID_Streets.id_np, ID_Streets.id_street, ID_Nps.id_region,\
                ID_Nps.id_atu, ID_Nps.id_selsov, ID_Nps.id_np, ID_Streets_history.id_np,\
                ID_Streets_history.id_street, ID_Streets_history.id_row,\
                Modify_reason.code_reason, Modify_reason.code_detail)

query2 = self.session.query(\
                sql.null().label('id_streets_id_np'),\
                sql.null().label('id_streets_id_street'),\
                sql.null().label('id_streets_name_street'),\
                sql.null().label('id_streets_type_street'),\
                ID_Streets_history, ID_Nps, Modify_reason)\
                .outerjoin(ID_Nps, ID_Nps.id_np == ID_Streets_history.id_np)\
                .outerjoin(Modify_reason, text('(ID_Streets_history.code_reason=Modify_reason.code_reason '\
                    'AND ID_Streets_history.code_detail=Modify_reason.code_detail)'))\
                .group_by(ID_Nps.id_region,\
                    ID_Nps.id_atu, ID_Nps.id_selsov, ID_Nps.id_np, ID_Streets_history.id_np,\
                    ID_Streets_history.id_street, ID_Streets_history.id_row,\
                    Modify_reason.code_reason, Modify_reason.code_detail)

query = query1.union(query2)

query2 = self.session.query(\
                sql.null().label('id_streets_id_np'),\
                sql.null().label('id_streets_id_street'),\
                sql.null().label('id_streets_name_street'),\
                sql.null().label('id_streets_type_street'),
                ID_Streets_history, ID_Nps, Modify_reason)\
                .select_from(ID_Streets_history, ID_Nps, Modify_reason)\
                .outerjoin(ID_Nps, ID_Nps.id_np == ID_Streets_history.id_np)\
                .outerjoin(Modify_reason, text(\
                    '(ID_Streets_history.code_reason=Modify_reason.code_reason '\
                    'AND ID_Streets_history.code_detail=Modify_reason.code_detail)'))

                .add_columns(User.user_id, User.name, User.class_year,User.primary_major,\
                    User.secondary_major, User.minor, User.primary_concentration,\
                    User.secondary_concentration, User.special_concentration,\
                    User.minor_concentration, Project.title, Project.abstract, Project.feature)\

                .add_columns(User.user_id.label("user_id"), User.name.label("name"), User.class_year.label("class_year"),User.primary_major.label("primary_major"),\
                    User.secondary_major.label("secondary_major"), User.minor.label("minor"), User.primary_concentration.label("primary_concentration"),\
                    User.secondary_concentration.label("secondary_concentration"), User.special_concentration.label("special_concentration"),\
                    User.minor_concentration.label("minor_concentration"), Project.title.label("title"), Project.abstract.label("abstract"), Project.feature.label("feature"))\


        # q = db.session.query(
        #     User
        # ).join(Project, (Project.user_id==User.user_id)
        # .with_entities(User.user_id, User.name, User.class_year,User.primary_major,\
        #     User.secondary_major, User.minor, User.primary_concentration,\
        #     User.secondary_concentration, User.special_concentration,\
        #     User.minor_concentration, Project.title, Project.abstract, Project.feature)\
        # ).filter(
        #     User.__ts_vector__.op('@@')(tq)
        # ).all()
        # print(q)