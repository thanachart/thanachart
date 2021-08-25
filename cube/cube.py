
def genCubeData(measures, dimensions, period):

  ## create time dimension
  def create_date_table(start, end):
  dayofweek={0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
  df = pd.DataFrame({"Date": pd.date_range(start, end)})
  df["Day"] = df.Date.dt.day
  df["Day of Week"] = df.Date.dt.dayofweek
  df["Day of Week"] = df["Day of Week"].map(dayofweek)
  df["Week"] = df.Date.dt.weekofyear
  df["Month"] = df.Date.dt.month
  df["Year"] = df.Date.dt.year
  return df

  df_time = create_date_table(period['StartDate'], period['EndDate'])

  ## generate dimension
  dims = []
  for key in dimensions.keys():
    dim_members = []
    for i in range(0, dimensions[key]):
      dim_members.append(key + ' ' + str(i+1))
    dims.append(dim_members)

  ## generate dimension members
  dim_row = []
  dim_index = []

  for element in itertools.product(*dims):
      dim_row.append(element)
      dim_index.append(np.random.exponential(1))

  df_dim = pd.DataFrame(dim_row, columns=dimensions.keys())

  ## merge df_time and df_dim
  df_time['key'] = 1
  df_dim['key'] = 1
  df = pd.merge(df_time, df_dim, on ='key').drop("key", 1)

  ## simulate data
  def generate_measure(seed):
    value = round(seed * np.random.exponential(1))
    return value

  for key in measures.keys():
    df[key] = 1
    df[key] = df[key].apply(lambda x: generate_measure(x))
  
  for dim in dimensions.keys():
    dim_index = random.sample(range(1, dimensions[dim] * 20), dimensions[dim])
    for i, j in enumerate(df[dim].unique()):    
      for measure in measures.keys():
        df.loc[df[dim]==j, measure] = (df.loc[df[dim]==j, measure] * (1+ dim_index[i]/sum(dim_index))).round()
  return df