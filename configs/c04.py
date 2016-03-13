# For mac local testing
configs = {}
configs[8] = {'batch_size': 10,
              'hidden_size': 10,
              'num_layers': 1,
              'rnn_num_layers': 2,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 100,
              'anneal_ratio': 0.5,
              'num_epochs': 1,
              'linear_start': False,
              'max_grad_norm': 40,
              'keep_prob': 1.0,
              'val_period': 1,
              'save_period': 1,
              'fold_path': 'data/s3-100/fold.json',
              'data_dir': 'data/s3-100',
              'model_name': 'm04',
              'mode': 'la',
              }

# debug purpose
configs[9] = {'batch_size': 100,
              'hidden_size': 100,
              'num_layers': 1,
              'rnn_num_layers': 1,
              'emb_num_layers': 1,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 100,
              'anneal_ratio': 0.5,
              'num_epochs': 100,
              'linear_start': False,
              'max_grad_norm': 40,
              'keep_prob': 1.0,
              'fold_path': 'data/s3/folds/fold11.json',
              'data_dir': 'data/s3_04_debug',
              'mode': 'la',
              'model_name': 'm04',
              'val_num_batches': 100}

# deploy configs start here
configs[0] = {'batch_size': 100,
              'hidden_size': 50,
              'num_layers': 1,
              'rnn_num_layers': 3,
              'emb_num_layers': 0,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 25,
              'anneal_ratio': 0.5,
              'num_epochs': 100,
              'keep_prob': 1.0,
              'fold_path': 'data/s3/folds/fold13.json',
              'data_dir': 'data/s3',
              'mode': 'a',
              'model_name': 'm04',
              'sim_func': 'dot',
              'lstm': 'basic',
              'forget_bias': 2.5,
              'cell_clip': 40,
              'model': 'sim',
              'rand_y': 1.0,
              }

configs[1] = {'batch_size': 100,
              'hidden_size': 50,
              'num_layers': 1,
              'rnn_num_layers': 3,
              'emb_num_layers': 0,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 25,
              'anneal_ratio': 0.5,
              'num_epochs': 100,
              'keep_prob': 1.0,
              'fold_path': 'data/s3/folds/fold13.json',
              'data_dir': 'data/s3',
              'mode': 'a',
              'model_name': 'm04',
              'sim_func': 'dot',
              'lstm': 'basic',
              'forget_bias': 2.5,
              'cell_clip': 40,
              'model': 'sim',
              'rand_y': 0.5,
              }

configs[2] = {'batch_size': 100,
              'hidden_size': 50,
              'num_layers': 1,
              'rnn_num_layers': 3,
              'emb_num_layers': 0,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 25,
              'anneal_ratio': 0.5,
              'num_epochs': 100,
              'keep_prob': 1.0,
              'fold_path': 'data/s3/folds/fold13.json',
              'data_dir': 'data/s3',
              'mode': 'a',
              'model_name': 'm04',
              'sim_func': 'dot',
              'lstm': 'basic',
              'forget_bias': 2.5,
              'cell_clip': 40,
              'model': 'sim',
              'rand_y': 1.0,
              'opt': 'adagrad',
              }

configs[3] = {'batch_size': 100,
              'hidden_size': 50,
              'num_layers': 1,
              'rnn_num_layers': 3,
              'emb_num_layers': 0,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 25,
              'anneal_ratio': 0.5,
              'num_epochs': 100,
              'keep_prob': 1.0,
              'fold_path': 'data/s3/folds/fold13.json',
              'data_dir': 'data/s3',
              'mode': 'a',
              'model_name': 'm04',
              'sim_func': 'dot',
              'lstm': 'basic',
              'forget_bias': 2.5,
              'cell_clip': 40,
              'model': 'sim',
              'rand_y': 0.5,
              'opt': 'adagrad',
              }

configs[4] = {'batch_size': 50,
              'hidden_size': 100,
              'num_layers': 1,
              'rnn_num_layers': 3,
              'emb_num_layers': 0,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 25,
              'anneal_ratio': 0.5,
              'num_epochs': 100,
              'keep_prob': 1.0,
              'fold_path': 'data/s3/folds/fold13.json',
              'data_dir': 'data/s3',
              'mode': 'a',
              'model_name': 'm04',
              'sim_func': 'dot',
              'lstm': 'basic',
              'forget_bias': 2.5,
              'cell_clip': 40,
              'model': 'sim',
              'rand_y': 1.0,
              }

configs[5] = {'batch_size': 50,
              'hidden_size': 100,
              'num_layers': 1,
              'rnn_num_layers': 3,
              'emb_num_layers': 0,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 25,
              'anneal_ratio': 0.5,
              'num_epochs': 100,
              'keep_prob': 1.0,
              'fold_path': 'data/s3/folds/fold13.json',
              'data_dir': 'data/s3',
              'mode': 'a',
              'model_name': 'm04',
              'sim_func': 'dot',
              'lstm': 'basic',
              'forget_bias': 2.5,
              'cell_clip': 40,
              'model': 'sim',
              'rand_y': 0.5,
              }

configs[6] = {'batch_size': 50,
              'hidden_size': 100,
              'num_layers': 1,
              'rnn_num_layers': 3,
              'emb_num_layers': 0,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 25,
              'anneal_ratio': 0.5,
              'num_epochs': 100,
              'keep_prob': 1.0,
              'fold_path': 'data/s3/folds/fold13.json',
              'data_dir': 'data/s3',
              'mode': 'a',
              'model_name': 'm04',
              'sim_func': 'dot',
              'lstm': 'basic',
              'forget_bias': 2.5,
              'cell_clip': 40,
              'model': 'sim',
              'rand_y': 1.0,
              'opt': 'adagrad',
              }

configs[7] = {'batch_size': 50,
              'hidden_size': 100,
              'num_layers': 1,
              'rnn_num_layers': 3,
              'emb_num_layers': 0,
              'init_mean': 0,
              'init_std': 0.1,
              'init_lr': 0.01,
              'anneal_period': 25,
              'anneal_ratio': 0.5,
              'num_epochs': 100,
              'keep_prob': 1.0,
              'fold_path': 'data/s3/folds/fold13.json',
              'data_dir': 'data/s3',
              'mode': 'a',
              'model_name': 'm04',
              'sim_func': 'dot',
              'lstm': 'basic',
              'forget_bias': 2.5,
              'cell_clip': 40,
              'model': 'sim',
              'rand_y': 0.5,
              'opt': 'adagrad',
              }
